from flask import Flask, jsonify
from kafka import KafkaConsumer
import json
import threading
import logging
import time
time.sleep(30)
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("smart-preprocessor")

KAFKA_TOPIC = "raw_energy_data"
KAFKA_SERVER = "kafka:9092"

def consume_from_kafka():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="earliest",
        group_id="smart-preprocessor-group"
    )
    for message in consumer:
        data = message.value
        logger.info("Preprocessing data: %s", data)
        # Here you can add transformation logic before sending to next node or topic

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "smart-preprocessor service running"})

if __name__ == "__main__":
    threading.Thread(target=consume_from_kafka, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)