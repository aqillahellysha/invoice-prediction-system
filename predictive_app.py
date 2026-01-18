# predictive_app.py
import streamlit as st
import pandas as pd
import joblib
import time
from log_utils import log_prediction

def run_app():
    st.header("⏱️ Invoice Processing Predictor")
    
    # 1. Load Models
    try:
        m1 = joblib.load('invoice_model_v1.pkl')
        m2 = joblib.load('invoice_model_v2.pkl')
    except:
        st.error("Models not found. Run training scripts first.")
        return

    # 2. Inputs
    c1, c2, c3 = st.columns(3)
    with c1:
        # Match these exactly to your dataset's user names
        user = st.selectbox("Processor", ["siti.farhana", "kanageswary.l", "weichung.t", "Others"])
    with c2:
        doc = st.selectbox("Doc Type", ["PO", "Non-PO", "Other Claims", "Foreign Vendor"])
    with c3:
        amt = st.number_input("Invoice Amount ($)", value=1000.0)

    # 3. Predict
    if st.button("Generate Estimate"):
        start = time.time()
        
        # Prepare DataFrame for model
        input_data = pd.DataFrame({
            'Invoice Amount': [amt], 
            'User Name': [user], 
            'Document Type': [doc]
        })
        
        # Predict
        p1 = m1.predict(input_data[['Invoice Amount']])[0]
        p2 = m2.predict(input_data)[0]
        latency = time.time() - start

        # Display
        st.success(f"Calculated in {latency:.4f}s")
        k1, k2 = st.columns(2)
        k1.metric("Model v1 (Basic)", f"{p1:.2f} Days")
        k2.metric("Model v2 (Smart)", f"{p2:.2f} Days", delta=f"{p1-p2:.2f} vs v1")

        # 4. Feedback
        with st.form("feedback_form"):
            st.write("Is this accurate?")
            score = st.slider("Rate (1-5)", 1, 5, 3)
            comment = st.text_input("Comments")
            if st.form_submit_button("Submit Log"):
                log_prediction(user, doc, amt, p1, p2, latency, score, comment)
                st.toast("Feedback Saved!")