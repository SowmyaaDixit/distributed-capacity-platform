# Distributed Capacity Platform

A real-time distributed system that simulates how modern platforms (e.g., Airbnb, NVIDIA) handle demand spikes by ingesting streaming data, detecting anomalies, forecasting capacity, and enabling intelligent scaling decisions.

---

## 🚀 Problem Statement

Modern systems face unpredictable demand spikes (traffic surges, GPU workloads, bookings).
This project simulates a production-grade pipeline that:

* Processes real-time events
* Detects anomalies in system load
* Forecasts future demand
* Enables capacity planning decisions

---

## 🏗️ Architecture

```
Producer → Kafka → Stream Processor → 
    ├── Forecasting Service
    ├── Anomaly Detection Service
    └── API Service → Dashboard
```

---

## ⚙️ Tech Stack

* Python (microservices)
* Kafka (event streaming)
* Docker (containerization)
* REST APIs (service communication)

---

## 🔥 Key Features

### 1. Real-time Streaming Pipeline

* Event-driven architecture using Kafka
* Handles continuous data ingestion

### 2. Anomaly Detection

* Identifies unusual spikes in load
* Helps detect failures or abnormal usage patterns

### 3. Demand Forecasting

* Predicts future capacity requirements
* Enables proactive scaling decisions

### 4. Fault Tolerance (Simulated)

* Retry mechanisms
* Idempotent processing
* Graceful failure handling

---

## 📊 System Metrics (Planned / Extendable)

* Throughput: events/sec
* Latency: end-to-end processing time
* Error rate
* Queue lag

---

## ⚠️ Failure Scenarios Considered

* Producer crash → recovery via message replay
* Consumer lag → backpressure handling
* Service failure → retry with exponential backoff

---

## 🧠 Design Decisions

* Event-driven architecture for scalability
* Loose coupling between services
* Eventual consistency for performance
* Partitioned streams for parallel processing

---

## 🚀 Getting Started

```bash
docker-compose up --build
```

---

## 📌 Future Improvements

* Add Prometheus + Grafana for observability
* Implement auto-scaling simulation logic
* Improve forecasting model (ML-based)
* Deploy on Kubernetes

---

## 💡 Why This Project

This project demonstrates:

* Distributed systems design
* Stream processing
* Scalability tradeoffs
* Real-world system thinking

---

## 👤 Author

Sowmyaa Dixit
