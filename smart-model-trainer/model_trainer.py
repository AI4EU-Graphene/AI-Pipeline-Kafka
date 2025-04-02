# smart-model-trainer/model_trainer.py

import os
import logging
from consumer import create_consumer
from trainer import train_model

INPUT_TOPIC = os.getenv("TRAINING_TOPIC", "preprocessed_data")
BATCH_SIZE = int(os.getenv("TRAINING_BATCH_SIZE", 1000))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ModelTrainer")

def main():
    consumer = create_consumer(INPUT_TOPIC)
    training_data = []

    logger.info(f"Listening to {INPUT_TOPIC} for training data...")

    for message in consumer:
        record = message.value
        training_data.append(record)

        if len(training_data) >= BATCH_SIZE:
            logger.info(f"Collected {BATCH_SIZE} samples. Starting training...")
            train_model(training_data)
            training_data.clear()  # Reset buffer

if __name__ == "__main__":
    main()