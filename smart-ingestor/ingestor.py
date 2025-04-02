# smart-ingestor/ingestor.py

import asyncio
import os
import logging
from producer import create_producer
from async_eirgrid_downloader import get_historic_data  # We'll refactor this in a bit

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "raw_energy_data")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SmartIngestor")

async def ingest_data():
    from httpx import AsyncClient
    producer = create_producer()

    async with AsyncClient(http2=True) as client:
        regions = ["ALL", "ROI", "NI"]
        for region in regions:
            logger.info(f"Fetching data for region: {region}")
            df = await get_historic_data(client, region)

            for _, row in df.iterrows():
                message = row.to_dict()
                producer.send(KAFKA_TOPIC, value=message)

            logger.info(f"Published {len(df)} rows for region: {region}")

if __name__ == "__main__":
    asyncio.run(ingest_data())