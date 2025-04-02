from flask import Flask, jsonify, request
import random
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "Smart Grid Rebalancer running"}), 200

@app.route("/rebalance", methods=["POST"])
def rebalance():
    data = request.json
    region_loads = data.get("region_loads", {})
    
    if not region_loads:
        return jsonify({"error": "No region loads provided"}), 400

    # Placeholder AI logic: flag regions above threshold and suggest shifts
    threshold = 75  # hypothetical threshold %
    suggestions = []

    for region, load in region_loads.items():
        if load > threshold:
            target_region = random.choice([r for r in region_loads if r != region])
            suggestions.append({
                "from": region,
                "to": target_region,
                "suggested_transfer_percent": round((load - threshold) * 0.8, 2)
            })

    logging.info("Rebalance suggestions: %s", suggestions)
    return jsonify({"rebalance_suggestions": suggestions}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)