# monitor_dashboard.py
import streamlit as st
import plotly.express as px
from log_utils import get_logs

def run_dashboard():
    st.header("📊 Performance Dashboard")
    df = get_logs()

    if df.empty:
        st.warning("No logs found. Make predictions first!")
        return

    # Metrics
    m1, m2 = st.columns(2)
    m1.metric("Total Invoices", len(df))
    m2.metric("Avg Feedback", f"{df['Feedback'].mean():.1f}/5")

    # Visuals
    st.subheader("Model Comparison")
    if len(df) > 1:
        fig = px.line(df, x='Timestamp', y=['Pred_v1', 'Pred_v2'], markers=True)
        st.plotly_chart(fig)
    else:
        st.info("Not enough data to plot trend line yet.")

    st.subheader("Recent Logs")
    st.dataframe(df.tail(5))