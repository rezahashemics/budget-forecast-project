Here is a professional and comprehensive **README.md** file for your project. This file is structured to match the **MVC/N-Tier architecture** and the technical requirements (ML, Security, and Budgeting) described in **Document 19.pdf**.

---

# 🏦 Bank Budget Prediction System

## 📖 Project Overview

This project implements an intelligent system for **Bank Budget Forecasting** using Machine Learning. Developed by **Seyed Reza Hashemi**, the system moves beyond traditional budgeting by utilizing real-time transaction data to predict future balances, operational costs, and cash flow.

The project follows a secure, modular architecture consisting of four integrated layers: Data, Security, Processing (ML), and Decision (UI).

---

## 🏗 System Architecture (MVC Layers)

### 1. Data Layer

Handles ingestion and cleaning of transaction records (Deposits, Withdrawals, and Balances).

* **Source:** CSV/Excel bank statements.
* **Preprocessing:** Normalization and Feature Engineering (Lagged Variables & Moving Averages).

### 2. Security Layer (Security-by-Design)

Implements industry-standard security protocols to protect sensitive financial data.

* **Encryption:** Uses **AES-256** for data at rest.
* **Fraud Detection:** Implements **Isolation Forest** algorithms to detect anomalies in transaction patterns.

### 3. Processing Layer (ML Models)

The "brain" of the system, implementing multiple predictive algorithms:

* **Linear Regression:** For baseline trend analysis.
* **Random Forest:** To handle non-linear financial patterns.
* **LSTM (Neural Networks):** For long-term time-series forecasting.

### 4. Decision Layer (Managerial Dashboard)

An interactive interface for bank managers to visualize predictions and risks.

* **Visualization:** Real-time charts of predicted vs. actual budget.
* **Alert System:** Visual indicators for detected security anomalies.

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.9+**
* **Poetry** (Python dependency manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/bank_budget_project.git
cd bank_budget_project

```


2. Install dependencies using Poetry:
```bash
poetry install

```



### Running the Application

To launch the interactive Decision Layer (Dashboard):

```bash
poetry run streamlit run app/controller.py

```

---

## 📂 Project Structure

```text
bank_budget_project/
├── app/
│   ├── models/          # Processing Layer (ML Algorithms)
│   ├── security/        # Security Layer (AES & Anomaly Detection)
│   ├── views/           # Decision Layer (Streamlit Dashboard)
│   └── controller.py    # System Orchestrator (MVC Controller)
├── data/                # Dataset storage (Raw & Processed)
├── pyproject.toml       # Poetry dependencies
└── README.md            # Project documentation

```

---

## 📊 Evaluation Metrics

The models are evaluated based on:

* **RMSE (Root Mean Squared Error):** To measure prediction accuracy.
* **MAE (Mean Absolute Error):** To understand the average magnitude of errors.
* **Anomaly Score:** To identify the percentage of suspicious activities.

## 🛡 Security & Compliance

This implementation aligns with:

* **ISO 27001** principles for data security.
* **Anomaly Detection** standards for modern digital banking fraud prevention.

---

## 👤 Author

* **Name:** Seyed Reza Hashemi
* **Instructor:** Dr. Zahra Koomleh
* **Academic Year:** 1404 (2025)

---

### 📝 License

This project is developed for educational purposes as part of the "Machine Learning in Banking" curriculum.
