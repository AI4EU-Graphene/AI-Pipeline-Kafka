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
logger = logging.getLogger("smart-anomaly-detector")

KAFKA_TOPIC_CONSUME = "forecast_data"
KAFKA_TOPIC_PRODUCE = "anomaly_results"
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
        group_id="anomaly-detector-group"
    )
    for message in consumer:
        data = message.value
        logger.info("smart-anomaly-detector consumed: %s", data)

        # Simulate anomaly detection
        forecast = data.get("forecast", 0)
        if forecast > 5000:  # Arbitrary threshold
            data["anomaly"] = True
        else:
            data["anomaly"] = False

        producer.send(KAFKA_TOPIC_PRODUCE, value=data)
        logger.info("smart-anomaly-detector produced: %s", data)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "smart-anomaly-detector service running"})

@app.route("/process", methods=["POST"])
def process_data():
    data = request.json
    logger.info("smart-anomaly-detector received data: %s", data)
    return jsonify({"status": "processed", "node": "smart-anomaly-detector"})

if __name__ == "__main__":
    threading.Thread(target=consume_data, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)