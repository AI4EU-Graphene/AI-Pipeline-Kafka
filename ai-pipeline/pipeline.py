from flask import Flask
from state_monitor import get_pipeline_state
from decision_engine import decide_pipeline_sequence, trigger_pipeline_sequence

app = Flask(__name__)

@app.route('/run-smart-pipeline', methods=['POST'])
def run_pipeline():
    state = get_pipeline_state()
    sequence = decide_pipeline_sequence(state)
    trigger_pipeline_sequence(sequence)
    return {"status": "Pipeline execution triggered", "sequence": sequence}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)