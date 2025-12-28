# app/views/dashboard.py
import streamlit as st
import matplotlib.pyplot as plt

def render_ui(data, predictions):
    st.set_page_config(page_title="Bank Decision Support System")
    st.title("🏦 Bank Budget Forecasting (Decision Layer)")

    st.sidebar.header("Security Status")
    anomalies = data[data['anomaly_score'] == -1]
    if not anomalies.empty:
        st.sidebar.error(f"⚠️ {len(anomalies)} Anomalies Detected!")

    st.subheader("Budget Forecast Analysis")
    fig, ax = plt.subplots()
    ax.plot(data.index, data['BALANCE AMT'], label="Actual", color="black")
    ax.plot(data.index, predictions['LinearRegression'], label="LR Forecast", linestyle="--")
    ax.legend()
    st.pyplot(fig)
