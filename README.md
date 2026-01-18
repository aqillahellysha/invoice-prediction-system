# 🧾 An Agile Data Science Application for Invoice Processing Time Prediction and Monitoring

## 📌 Project Overview
This project implements an **Agile Machine Learning pipeline** to predict the time required to process financial invoices. It addresses the business problem of **resource allocation** by allowing Team Leads to estimate workload and Managers to monitor team efficiency.

# 🧩 Agile Development Overview

This project was developed using an Agile, sprint-based approach to support iterative model improvement and system enhancement.

Key iterations include:
- **Sprint 1:** Data preparation and baseline model development (Model v1)
- **Sprint 2:** Model improvement and prediction application development (Model v2)
- **Sprint 3:** Monitoring dashboard implementation and evaluation

Detailed user stories, product backlog, sprint planning, and iteration analysis are documented in the accompanying case study report.

## 🚀 Key Features
* **Model v1 (Baseline):** Linear Regression using only `Invoice Amount`.
* **Model v2 (Production):** Random Forest Regressor using `User Name`, `Document Type`, and `Amount`.
* **Predictive App:** Streamlit interface for real-time estimations.
* **Monitoring Dashboard:** Tracks model accuracy, latency, and user feedback.

## 🛠️ Installation & Usage
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/aqillahellysha/invoice-prediction-system.git](https://github.com/aqillahellysha/invoice-prediction-systemt)
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Clone the repo:**
   ```bash
   streamlit run main.py
