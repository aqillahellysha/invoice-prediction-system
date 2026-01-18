import pandas as pd
import os
from datetime import datetime

# Force the file to be in the current folder
file_path = os.path.abspath("monitoring_logs.csv")

print(f"Creating log file at: {file_path}")

data = {
    'Timestamp': [datetime.now(), datetime.now()],
    'User': ['TEST_USER_1', 'TEST_USER_2'],
    'Doc_Type': ['PO', 'Non-PO'],
    'Amount': [1000.0, 5000.0],
    'Pred_v1': [1.5, 2.0],
    'Pred_v2': [1.2, 2.2],
    'Latency': [0.05, 0.04],
    'Feedback': [5, 3],
    'Comments': ['Test comment 1', 'Test comment 2']
}

df = pd.DataFrame(data)
df.to_csv("monitoring_logs.csv", index=False)

print("SUCCESS! File created. Check your folder.")