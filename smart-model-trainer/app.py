
from flask import Flask, jsonify, request
import logging
import time
time.sleep(30)
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("smart-model-trainer")

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "smart-model-trainer service running"})

@app.route("/process", methods=["POST"])
def process_data():
    data = request.json
    logger.info("smart-model-trainer received data: %s", data)
    return jsonify({"status": "processed", "node": "smart-model-trainer"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
