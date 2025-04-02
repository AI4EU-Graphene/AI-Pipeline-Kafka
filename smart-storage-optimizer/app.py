from flask import Flask, jsonify
from kafka import KafkaConsumer
import json
import threading
import time

app = Flask(__name__)

# Simulated storage levels
storage_state = {
    "level": 50.0,  # in %
    "charging": False
}

# Optimization logic (placeholder for ML)
def optimize_storage():
    consumer = KafkaConsumer(
        'forecast_output',
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='latest',
        group_id='storage-optimizer-group'
    )
    
    for message in consumer:
        forecast = message.value.get("forecast", 0)
        current_storage = storage_state["level"]

        # Simple logic: Charge if forecast low, discharge if high
        if forecast < 50 and current_storage < 80:
            storage_state["level"] += 2  # charge
            storage_state["charging"] = True
        elif forecast >= 50 and current_storage > 20:
            storage_state["level"] -= 2  # discharge
            storage_state["charging"] = False
        else:
            storage_state["charging"] = False

        print(f"Updated storage: {storage_state}")
        time.sleep(2)

# Background thread
threading.Thread(target=optimize_storage, daemon=True).start()

@app.route("/")
def status():
    return jsonify(storage_state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)