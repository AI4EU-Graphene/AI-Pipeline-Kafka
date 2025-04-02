# smart-model-trainer/app.py

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    return {"status": "smart-model-trainer is running"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)