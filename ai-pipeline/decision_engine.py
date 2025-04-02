def decide_pipeline_sequence(state):
    sequence = []
    if state.get("trainer") == "ready":
        sequence.append("trainer")
    if state.get("preprocessor") == "ready":
        sequence.append("preprocessor")
    if state.get("ml_preprocessor") == "ready":
        sequence.append("ml_preprocessor")
    if state.get("forecaster") == "ready":
        sequence.append("forecaster")
    if state.get("detector") == "ready":
        sequence.append("detector")
    if state.get("alert") == "ready":
        sequence.append("alert")
    if state.get("ingestor") == "ready":
        sequence.append("ingestor")
    return sequence

def trigger_pipeline_sequence(sequence):
    for service in sequence:
        try:
            print(f"Triggering: {service}")
            requests.post(f"http://smart-{service}:5000/trigger")
        except Exception as e:
            print(f"Failed to trigger {service}: {e}")