# smart-anomaly-detector/app.py

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    return {"status": "smart-anomaly-detector is running"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)