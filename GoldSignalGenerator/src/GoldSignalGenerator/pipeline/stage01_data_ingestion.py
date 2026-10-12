from GoldSignalGenerator.components.data_ingestion import DataIngestion


def main():
    try:
        ingestion = DataIngestion(
            api_key="8f5afc8625b4427683cdfc5af6c60f3d",
            symbol="XAU/USD",
            interval="1h"
        )
        output_path = ingestion.initiate_data_ingestion()
        print(f"🎉 Data ingestion successful! File saved at:\n{output_path}")

    except Exception as e:
        print(f"❌ Error during ingestion: {e}")


if __name__ == "__main__":
    main()
