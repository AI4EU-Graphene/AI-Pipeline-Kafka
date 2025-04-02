# smart-ml-preprocessor/ml_preprocessor.py

import os
import logging
from producer import create_producer
from consumer import create_consumer
from feature_engineer import FeatureEngineer

RAW_TOPIC = os.getenv("CLEANED_TOPIC", "preprocessed_data")
ML_READY_TOPIC = os.getenv("ML_READY_TOPIC", "ml_ready_data")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MLPreprocessor")

def main():
    consumer = create_consumer(RAW_TOPIC)
    producer = create_producer()
    fe = FeatureEngineer()

    logger.info(f"Listening to topic: {RAW_TOPIC}")

    for message in consumer:
        record = message.value
        features = fe.transform(record)

        if features:
            producer.send(ML_READY_TOPIC, value=features)
            logger.info(f"Published ML-ready record to {ML_READY_TOPIC}")
        else:
            logger.info("Waiting for more historical data...")

if __name__ == "__main__":
    main()