from flask import Flask, jsonify, request
import logging
from kafka import KafkaConsumer
import threading
import json
import time
time.sleep(30)
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("smart-grid-rebalancer")

KAFKA_TOPIC = "alert_signals"
KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"

def consume_data():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        group_id="grid-rebalancer-group"
    )
    for message in consumer:
        data = message.value
        logger.info("smart-grid-rebalancer received signal: %s", data)
        logger.info("Executing rebalancing strategy...")

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "smart-grid-rebalancer service running"})

@app.route("/process", methods=["POST"])
def process_data():
    data = request.json
    logger.info("smart-grid-rebalancer received data: %s", data)
    return jsonify({"status": "processed", "node": "smart-grid-rebalancer"})

if __name__ == "__main__":
    threading.Thread(target=consume_data, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)