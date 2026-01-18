# log_utils.py
import pandas as pd
import os
from datetime import datetime

LOG_FILE = 'monitoring_logs.csv'

def log_prediction(user, doc, amount, p1, p2, latency, feedback, comments):
    # Prepare data row
    data = {
        'Timestamp': [datetime.now()],
        'User': [user],
        'Doc_Type': [doc],
        'Amount': [amount],
        'Pred_v1': [p1],
        'Pred_v2': [p2],
        'Latency': [latency],
        'Feedback': [feedback],
        'Comments': [comments]
    }
    df = pd.DataFrame(data)
    
    # Append to CSV (create if doesn't exist)
    if not os.path.exists(LOG_FILE):
        df.to_csv(LOG_FILE, index=False)
    else:
        df.to_csv(LOG_FILE, mode='a', header=False, index=False)

def get_logs():
    if os.path.exists(LOG_FILE):
        return pd.read_csv(LOG_FILE)
    return pd.DataFrame()