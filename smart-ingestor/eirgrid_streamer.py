import os
import pandas as pd
from kafka import KafkaProducer
import json
from async_eirgrid_downloader import main as download_data_main

def collect_csv_paths(base_dir="Downloaded_Data"):
    paths = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".csv"):
                paths.append(os.path.join(root, file))
    return paths

def stream_csv_to_kafka(csv_paths, topic="raw_energy_data", kafka_server="kafka:9092"):
    producer = KafkaProducer(
        bootstrap_servers=kafka_server,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    for path in csv_paths:
        try:
            df = pd.read_csv(path, header=None)
            for _, row in df.iterrows():
                producer.send(topic, row.to_dict())
        except Exception as e:
            print(f"⚠️ Skipped {path}: {e}")
    
    producer.flush()
    print("✅ Finished streaming data to Kafka.")

def run():
    print("📥 Starting EirGrid data download...")
    download_data_main()
    print("📦 Collecting CSV files...")
    csv_paths = collect_csv_paths()
    print(f"📤 Streaming {len(csv_paths)} CSV files to Kafka...")
    stream_csv_to_kafka(csv_paths)