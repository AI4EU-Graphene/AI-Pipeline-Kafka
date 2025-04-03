from flask import Flask
import logging
from state_monitor import get_pipeline_state
from decision_engine import decide_pipeline_sequence, trigger_pipeline_sequence

# Configure logging
logging.basicConfig(
    filename='pipeline_debug.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

@app.route('/run-smart-pipeline', methods=['POST'])
def run_pipeline():
    logging.info("Smart pipeline execution triggered")
    
    # Get the current state of all nodes
    state = get_pipeline_state()
    logging.info(f"Pipeline state fetched: {state}")
    
    # Decide execution sequence based on state
    sequence = decide_pipeline_sequence(state)
    logging.info(f"Pipeline sequence decided: {sequence}")
    
    # Trigger the pipeline
    trigger_pipeline_sequence(sequence)
    
    return {"status": "Pipeline execution triggered", "sequence": sequence}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)