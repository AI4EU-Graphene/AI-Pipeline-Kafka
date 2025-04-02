# smart-preprocessor/cleaner.py

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Cleaner")

def clean_record(record: dict) -> dict:
    try:
        # Convert timestamp to standard ISO
        record["timestamp"] = pd.to_datetime(record["timestamp"]).isoformat()

        # Ensure numeric fields are properly casted
        numeric_fields = ["demand", "forecast", "generation"]
        for field in numeric_fields:
            record[field] = float(record.get(field, 0.0))

        # Fill missing or out-of-bounds values
        for key, value in record.items():
            if value is None or (isinstance(value, float) and (pd.isna(value) or value < 0)):
                record[key] = 0.0

        return record

    except Exception as e:
        logger.warning(f"Failed to clean record: {e}")
        return None