from flask import Flask, jsonify, request
import logging
from kafka import KafkaConsumer, KafkaProducer
import threading
import json
import time
time.sleep(30)
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("smart-ml-forecaster")

KAFKA_TOPIC_CONSUME = "ml_ready_data"
KAFKA_TOPIC_PRODUCE = "forecast_data"
KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def consume_data():
    consumer = KafkaConsumer(
        KAFKA_TOPIC_CONSUME,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        group_id="ml-forecaster-group"
    )
    for message in consumer:
        data = message.value
        logger.info("smart-ml-forecaster consumed: %s", data)

        # Simulate forecasting
        data["forecast"] = data.get("Value", 0) * 1.05  # Mock forecast logic
        producer.send(KAFKA_TOPIC_PRODUCE, value=data)

        logger.info("smart-ml-forecaster produced: %s", data)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "smart-ml-forecaster service running"})

@app.route("/process", methods=["POST"])
def process_data():
    data = request.json
    logger.info("smart-ml-forecaster received data: %s", data)
    return jsonify({"status": "processed", "node": "smart-ml-forecaster"})

if __name__ == "__main__":
    threading.Thread(target=consume_data, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)