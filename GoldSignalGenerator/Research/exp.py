# %% [markdown]
# ## 4 Hourly Data

# %%
import pandas as pd
import glob

# %%
files = glob.glob("/Users/mac/Desktop/Upwork/GoldSignalGenerator/Artifacts/HourlyData/XAU-USD_Hour_*.csv")
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# %%
df.head()

# %%
df["UTC"] = pd.to_datetime(
    df["UTC"], 
    format="%d.%m.%Y %H:%M:%S.%f UTC"
)

df = df.sort_values("UTC", ascending=True).reset_index(drop=True)
df.rename(columns={'UTC':'datetime'}, inplace=True)

# %%
print(df.head())

# %%
print(df.tail())

# %%
df.info()

# %%
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Load your 4-hour data
# df = pd.read_csv('your_4hour_data.csv')
df['datetime'] = pd.to_datetime(df['datetime'])
df = df.sort_values('datetime').reset_index(drop=True)

print(f"Total candles: {len(df)}")
print(f"Date range: {df['datetime'].min()} to {df['datetime'].max()}")
print(f"Duration: {(df['datetime'].max() - df['datetime'].min()).days} days")
print(f"Missing values: {df.isnull().sum().sum()}")

# Time features
df['hour'] = df['datetime'].dt.hour
df['day_of_week'] = df['datetime'].dt.dayofweek
df['month'] = df['datetime'].dt.month
df['year'] = df['datetime'].dt.year

# %%
def add_technical_indicators(df):
    """Add technical indicators for 4-hour timeframe"""
    df = df.copy()
    
    # Moving Averages
    df['SMA_10'] = df['Close'].rolling(window=10).mean()  # 40 hours
    df['SMA_20'] = df['Close'].rolling(window=20).mean()  # 80 hours (~3 days)
    df['SMA_50'] = df['Close'].rolling(window=50).mean()  # 200 hours (~8 days)
    df['SMA_100'] = df['Close'].rolling(window=100).mean()  # 400 hours (~17 days)
    
    df['EMA_10'] = df['Close'].ewm(span=10, adjust=False).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['EMA_50'] = df['Close'].ewm(span=50, adjust=False).mean()
    
    # RSI
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # MACD
    ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = ema_12 - ema_26
    df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    df['MACD_Histogram'] = df['MACD'] - df['MACD_Signal']
    
    # Bollinger Bands
    df['BB_Middle'] = df['Close'].rolling(window=20).mean()
    bb_std = df['Close'].rolling(window=20).std()
    df['BB_Upper'] = df['BB_Middle'] + (bb_std * 2)
    df['BB_Lower'] = df['BB_Middle'] - (bb_std * 2)
    df['BB_Width'] = (df['BB_Upper'] - df['BB_Lower']) / df['BB_Middle']
    
    # ATR (for stop loss)
    high_low = df['High'] - df['Low']
    high_close = abs(df['High'] - df['Close'].shift())
    low_close = abs(df['Low'] - df['Close'].shift())
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    df['ATR'] = tr.rolling(window=14).mean()
    
    # Momentum
    df['ROC'] = ((df['Close'] - df['Close'].shift(10)) / df['Close'].shift(10)) * 100
    df['Momentum'] = df['Close'] - df['Close'].shift(10)
    
    # Volume
    df['Volume_MA'] = df['Volume'].rolling(window=20).mean()
    df['Volume_Ratio'] = df['Volume'] / df['Volume_MA']
    
    # Price position
    df['Price_to_SMA20'] = (df['Close'] - df['SMA_20']) / df['SMA_20']
    df['Price_to_SMA50'] = (df['Close'] - df['SMA_50']) / df['SMA_50']
    
    # Trend indicators
    df['SMA10_above_SMA20'] = (df['SMA_10'] > df['SMA_20']).astype(int)
    df['SMA20_above_SMA50'] = (df['SMA_20'] > df['SMA_50']).astype(int)
    df['Price_above_SMA50'] = (df['Close'] > df['SMA_50']).astype(int)
    
    # Volatility
    df['Returns'] = df['Close'].pct_change()
    df['Volatility'] = df['Returns'].rolling(window=20).std()
    
    return df

df = add_technical_indicators(df)
df = df.dropna()

print(f"\nAfter adding indicators: {len(df)} candles")
print(f"Features created: {df.shape[1]} columns")

# %%
def create_target(df, forward_periods=1, threshold=0.003):
    """
    Create target for NEXT candle (4 hours ahead)
    threshold = 0.3% minimum move to consider tradeable
    """
    df = df.copy()
    
    # Look 1 period ahead (4 hours)
    df['Future_Close'] = df['Close'].shift(-forward_periods)
    df['Future_Return'] = (df['Future_Close'] - df['Close']) / df['Close']
    
    # Classify
    def classify(ret):
        if pd.isna(ret):
            return np.nan
        elif ret > threshold:
            return 1  # BUY
        elif ret < -threshold:
            return -1  # SELL
        else:
            return 0  # HOLD
    
    df['Target'] = df['Future_Return'].apply(classify)
    
    return df

df = create_target(df, forward_periods=1, threshold=0.003)
df = df.dropna()

print("\nTarget Distribution:")
print(df['Target'].value_counts().sort_index())
print("\nPercentages:")
print(df['Target'].value_counts(normalize=True).sort_index() * 100)

# %%
df.head()

# %%
df.info(max_cols=100)

# %%
df["Target"].value_counts()

# %%
from prophet import Prophet

def add_prophet_features(df):
    try:
        prophet_df = df[['datetime', 'Close']].rename(columns={'datetime': 'ds', 'Close': 'y'})
        prophet_df['ds'] = pd.to_datetime(prophet_df['ds']).dt.tz_localize(None)

        model = Prophet(
            daily_seasonality=True,
            weekly_seasonality=True,
            yearly_seasonality=False,
            seasonality_mode='additive',
            interval_width=0.8,
            changepoint_prior_scale=0.05,
            seasonality_prior_scale=0.1
        )
        model.fit(prophet_df)

        forecast = model.predict(prophet_df[['ds']])
        forecast_features = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper', 'trend']]
        df = df.merge(forecast_features, left_on='datetime', right_on='ds', how='left').drop(columns=['ds'])

        return df

    except Exception as e:
        print(f"Prophet failed: {e}")
        return df


# %%
df = add_prophet_features(df)

# %%
df.head()

# %%
df.info()

# %%
import numpy as np
import pandas as pd
import ta  

def add_features(df, return_horizons=[5, 10, 30]):

    df = df.copy()

    # --- 1. TA Indicators ---
    # On-Balance Volume (OBV)
    df['OBV'] = ta.volume.OnBalanceVolumeIndicator(
        close=df['Close'], volume=df['Volume']).on_balance_volume()

    # Commodity Channel Index (CCI)
    df['CCI'] = ta.trend.CCIIndicator(
        high=df['High'], low=df['Low'], close=df['Close'], window=20).cci()

    # Average Directional Movement Index (ADX)
    df['ADX'] = ta.trend.ADXIndicator(
        high=df['High'], low=df['Low'], close=df['Close'], window=14).adx()

    # Williams %R
    df['WilliamsR'] = ta.momentum.WilliamsRIndicator(
        high=df['High'], low=df['Low'], close=df['Close'], lbp=14).williams_r()

    # Parabolic SAR
    df['Parabolic_SAR'] = ta.trend.PSARIndicator(
        high=df['High'], low=df['Low'], close=df['Close']).psar()

    # Chaikin Money Flow
    df['CMF'] = ta.volume.ChaikinMoneyFlowIndicator(
        high=df['High'], low=df['Low'], close=df['Close'], volume=df['Volume']).chaikin_money_flow()

    # Stochastic RSI
    df['StochRSI'] = ta.momentum.StochRSIIndicator(
        close=df['Close'], window=14).stochrsi()

    # Accumulation/Distribution Index
    df['ADI'] = ta.volume.AccDistIndexIndicator(
        high=df['High'], low=df['Low'], close=df['Close'], volume=df['Volume']).acc_dist_index()

    # Force Index
    df['ForceIndex'] = ta.volume.ForceIndexIndicator(
        close=df['Close'], volume=df['Volume']).force_index()

    # Money Flow Index (MFI)
    df['MFI'] = ta.volume.MFIIndicator(
        high=df['High'], low=df['Low'], close=df['Close'], volume=df['Volume']).money_flow_index()

    # --- 2. Cyclical Time Features ---
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)

    df['day_sin'] = np.sin(2 * np.pi * df['datetime'].dt.day / 31)
    df['day_cos'] = np.cos(2 * np.pi * df['datetime'].dt.day / 31)

    df['dayofweek_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 7)
    df['dayofweek_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 7)

    # --- 3. Multi-horizon Targets ---
    for horizon in return_horizons:
        df[f'Future_Return_{horizon}m'] = (
            df['Close'].shift(-horizon) - df['Close']
        ) / df['Close']

    return df


# %%
df = add_features(df)
df.head()

# %%
df.info()

# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def split_scale_timeseries(df, target_col="Target", train_size=0.7, val_size=0.15):

    df = df.copy()

    X = df.drop(columns=[target_col, 'datetime'])
    y = df[target_col].values

    n = len(df)
    train_end = int(n * train_size)
    val_end = int(n * (train_size + val_size))

    X_train, y_train = X.iloc[:train_end], y[:train_end]
    X_val, y_val = X.iloc[train_end:val_end], y[train_end:val_end]
    X_test, y_test = X.iloc[val_end:], y[val_end:]

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)

    return (X_train_scaled, y_train,
            X_val_scaled, y_val,
            X_test_scaled, y_test,
            scaler)


# %%
X_train, y_train, X_val, y_val, X_test, y_test, scaler = split_scale_timeseries(df)

print("Train shape:", X_train.shape)
print("Val shape:", X_val.shape)
print("Test shape:", X_test.shape)


# %%
import xgboost as xgb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, classification_report

def train_xgboost_precision(X_train, y_train, X_val, y_val, X_test, y_test, target_precision=0.8):
    # Ensure binary labels (0/1)
    y_train = (y_train > 0).astype(int)
    y_val   = (y_val > 0).astype(int)
    y_test  = (y_test > 0).astype(int)

    # Convert to DMatrix
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dval   = xgb.DMatrix(X_val, label=y_val)
    dtest  = xgb.DMatrix(X_test, label=y_test)

    params = {
        "objective": "binary:logistic",
        "eval_metric": "logloss",
        "eta": 0.05,
        "max_depth": 6,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "seed": 42
    }

    evals = [(dtrain, "train"), (dval, "val")]
    model = xgb.train(
        params,
        dtrain,
        num_boost_round=1000,
        evals=evals,
        early_stopping_rounds=50,
        verbose_eval=50
    )

    # -------------------
    # Find best threshold for precision
    # -------------------
    y_val_proba = model.predict(dval)

    thresholds = np.arange(0.1, 0.9, 0.01)
    precisions = []

    for t in thresholds:
        preds = (y_val_proba > t).astype(int)
        precisions.append(precision_score(y_val, preds, zero_division=0))

    best_idx = np.argmax(precisions)
    best_thresh = thresholds[best_idx]
    best_precision = precisions[best_idx]

    print(f"\nBest Threshold: {best_thresh:.2f} | Precision: {best_precision:.3f}")

    # -------------------
    # Apply best threshold
    # -------------------
    y_val_pred = (y_val_proba > best_thresh).astype(int)
    print("\nValidation Report:")
    print(classification_report(y_val, y_val_pred))

    y_test_proba = model.predict(dtest)
    y_test_pred = (y_test_proba > best_thresh).astype(int)

    print("\nTest Report (using tuned threshold):")
    print(classification_report(y_test, y_test_pred))

    # Plot precision vs threshold
    plt.figure(figsize=(6,4))
    plt.plot(thresholds, precisions, marker='o')
    plt.axhline(target_precision, color='r', linestyle='--', label=f'Target Precision {target_precision}')
    plt.axvline(best_thresh, color='g', linestyle='--', label=f'Best Thresh {best_thresh:.2f}')
    plt.xlabel("Threshold")
    plt.ylabel("Precision")
    plt.title("Precision vs Threshold")
    plt.legend()
    plt.show()

    return model, best_thresh


# %%
model, best_thresh = train_xgboost_precision(X_train, y_train, X_val, y_val, X_test, y_test, target_precision=0.8)


# %%



