# main.py
import streamlit as st
from predictive_app import run_app
from monitor_dashboard import run_dashboard

st.set_page_config(page_title="Invoice AI", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Prediction Tool", "Monitoring Dashboard"])

if page == "Prediction Tool":
    run_app()
else:
    run_dashboard()