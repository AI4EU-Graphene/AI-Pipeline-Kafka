# ⚡ AI-Pipeline for Real-Time Smart Grid Energy Management

This project implements an **AI-powered, self-adaptive pipeline** for smart grid energy forecasting, preprocessing, training, and alerting using **Apache Kafka**, **Flask microservices**, and **ML intelligence** to auto-select the pipeline flow based on live context and learned patterns.

---

## 📌 Project Goals

- Fully automated ML pipeline for grid data analysis
- Real-time energy forecasting and anomaly detection
- Kafka-based decoupled communication across services
- Self-learning AI orchestrator deciding optimal pipeline flow
- Plug-n-play architecture: `docker-compose up` and go!

---

## 🧠 AI-Driven Pipeline Logic

Instead of traditional orchestration via fixed logic, this system uses a smart decision engine that learns patterns from past runs, system states, and runtime metrics to:

- Decide **which services to run and in what order**
- Bypass unnecessary nodes when confidence is high
- Trigger model retraining dynamically
- Adjust paths based on seasonal/time-of-day/weekly patterns

---

## ⚙️ System Architecture

![AI Pipeline Architecture](AI_Pipeline_Architecture.png)

### 🔧 Nodes (Microservices)

| Node | Description |
|------|-------------|
| `smart-ingestor` | Downloads raw energy data and streams to Kafka |
| `smart-preprocessor` | Cleans and validates raw data |
| `smart-ml-preprocessor` | Feature engineering and scaling |
| `smart-model-trainer` | Trains model if needed |
| `smart-ml-forecaster` | Generates live energy forecasts |
| `smart-anomaly-detector` | Detects grid anomalies from forecasts |
| `smart-alert-engine` | Sends alerts on anomalies or outages |
| `smart-grid-rebalancer` | Suggests redistribution actions |
| `smart-storage-optimizer` | Optimizes battery/storage use |
| `ai-pipeline-manager` | ML-based orchestrator for smart routing |

---

## 🚀 Usage

```bash
git clone git@github.com:AI4EU-Graphene/AI-Pipeline-Kafka.git
cd AI-Pipeline-Kafka
docker-compose up --build
```

---

## 📂 Folder Structure

```
AI-Pipeline-Kafka/
├── ai-pipeline-manager/
├── smart-alert-engine/
├── smart-anomaly-detector/
├── smart-grid-rebalancer/
├── smart-ingestor/
├── smart-ml-forecaster/
├── smart-ml-preprocessor/
├── smart-model-trainer/
├── smart-preprocessor/
├── smart-storage-optimizer/
├── kafka/
│   ├── kafka.Dockerfile
│   └── zookeeper.Dockerfile
├── docker-compose.yaml
├── AI_Pipeline_Architecture.png
└── README.md
```

---

## 🌐 Powered By

- Python, Flask
- Apache Kafka & Zookeeper
- Scikit-learn, pandas, httpx
- Docker, Compose
- Real-time Smart Grid APIs (e.g., EirGrid)

---

## 👨‍🔬 Designed With

- 💡 Modularity
- 🧠 ML-first orchestration
- 🔁 Self-healing & continuous learning
- ⚙️ Minimal setup for non-technical users

---

## 📣 Contributors

- **@gunx-ai** (Creator, Vision)
- **ChatGPT** (Architect, Engineer)

---

**📦 Just plug & play. The AI handles the rest.**