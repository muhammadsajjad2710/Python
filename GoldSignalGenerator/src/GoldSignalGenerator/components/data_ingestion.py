import os
import requests
import pandas as pd
import datetime


class DataIngestion:
    def __init__(self,
                 api_key: str,
                 artifact_dir: str = "Artifacts/12data",
                 symbol: str = "XAU/USD",
                 interval: str = "1h"):

        self.api_key = api_key
        self.symbol = symbol
        self.interval = interval
        self.base_url = "https://api.twelvedata.com/time_series"
        self.artifact_dir = artifact_dir

        os.makedirs(self.artifact_dir, exist_ok=True)
        self.output_file_path = os.path.join(
            self.artifact_dir,
            f"gld_timeframe_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        )

    def _fetch_chunk(self, start_date: str, end_date: str) -> pd.DataFrame:

        params = {
            "symbol": self.symbol,
            "interval": self.interval,
            "start_date": start_date,
            "end_date": end_date,
            "apikey": self.api_key,
            "format": "json",
            "outputsize": 5000
        }

        print(f"📡 Fetching from {start_date} → {end_date}")
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if "values" not in data:
            print("⚠️ No data for this range:", data.get("message", ""))
            return pd.DataFrame()

        df = pd.DataFrame(data["values"])
        df["UTC"] = pd.to_datetime(df["datetime"], errors="coerce", utc=True)
        df = df.rename(columns={
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "volume": "Volume"
        })

        cols = ["UTC", "Open", "High", "Low", "Close"]
        if "Volume" in df.columns:
            cols.append("Volume")
        df = df[cols]

        for col in ["Open", "High", "Low", "Close"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df = df.dropna(subset=["UTC"]).sort_values("UTC").reset_index(drop=True)
        return df

    def _fetch_all_chunks(self) -> pd.DataFrame:

        end_dt = datetime.datetime.utcnow()
        start_dt = end_dt - datetime.timedelta(days=3 * 365)

        # Define 3 date segments (approx 1 year each, within 5000-row limits)
        date_ranges = [
            (start_dt, start_dt + datetime.timedelta(days=365)),
            (start_dt + datetime.timedelta(days=365), start_dt + datetime.timedelta(days=730)),
            (start_dt + datetime.timedelta(days=730), end_dt)
        ]

        all_dfs = []
        for start, end in date_ranges:
            df_chunk = self._fetch_chunk(
                start.strftime("%Y-%m-%d %H:%M:%S"),
                end.strftime("%Y-%m-%d %H:%M:%S")
            )
            if not df_chunk.empty:
                all_dfs.append(df_chunk)

        if not all_dfs:
            raise ValueError("❌ No data fetched from TwelveData API.")

        print("🔄 Merging all chunks...")
        combined_df = pd.concat(all_dfs, ignore_index=True)
        combined_df = combined_df.drop_duplicates(subset=["UTC"], keep="last")
        combined_df = combined_df.sort_values("UTC").reset_index(drop=True)
        print(f"✅ Combined shape: {combined_df.shape}")
        return combined_df

    def initiate_data_ingestion(self) -> str:

        df = self._fetch_all_chunks()
        df.to_csv(self.output_file_path, index=False)
        print(f"💾 Saved merged file: {self.output_file_path}")
        return self.output_file_path
