# smart-ml-forecaster/model_loader.py

import time
import joblib
import os
import logging

MODEL_PATH = os.getenv("MODEL_PATH", "model/latest_model.pkl")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ModelLoader")

def wait_for_model(path=MODEL_PATH, timeout=300, check_interval=5):
    logger.info(f"Waiting for model file at {path}...")

    waited = 0
    while not os.path.exists(path):
        time.sleep(check_interval)
        waited += check_interval
        if waited >= timeout:
            raise FileNotFoundError(f"Model file not found after {timeout} seconds")
        logger.info("Model not yet available... retrying")

    logger.info("Model found. Loading...")
    model = joblib.load(path)
    logger.info("Model loaded successfully.")
    return model