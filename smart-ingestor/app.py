from flask import Flask
from eirgrid_streamer import run

app = Flask(__name__)

@app.route("/")
def health_check():
    return "✅ Smart Ingestor is live!"

@app.route("/trigger", methods=["POST"])
def trigger_stream():
    try:
        run()
        return "✅ Data ingestion and streaming started.", 200
    except Exception as e:
        return f"❌ Error during ingestion: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)