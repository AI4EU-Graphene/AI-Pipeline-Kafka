# smart-ml-forecaster/ml_forecaster.py

import os
import logging
from producer import create_producer
from consumer import create_consumer
from model_loader import wait_for_model
from forecaster import predict

INPUT_TOPIC = os.getenv("ML_READY_TOPIC", "ml_ready_data")
OUTPUT_TOPIC = os.getenv("FORECAST_TOPIC", "forecast_output")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MLForecaster")

def main():
    consumer = create_consumer(INPUT_TOPIC)
    producer = create_producer()
    model = wait_for_model()

    logger.info(f"Listening to {INPUT_TOPIC} for predictions...")

    for message in consumer:
        features = message.value
        forecast_record = predict(model, features)

        if forecast_record:
            producer.send(OUTPUT_TOPIC, value=forecast_record)
            logger.info(f"Published forecast for {forecast_record['timestamp']}")
        else:
            logger.warning("Skipping bad feature input")

if __name__ == "__main__":
    main()