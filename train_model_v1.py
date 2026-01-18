# train_model_v1.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

print("--- Training Model v1 (Baseline) ---")

# 1. Load Data (Added encoding fix here)
df = pd.read_csv('invoice_data.csv', encoding='ISO-8859-1')

# 2. Data Cleaning
# Remove commas from 'Invoice Amount'
df['Invoice Amount'] = df['Invoice Amount'].astype(str).str.replace(',', '', regex=False)
df['Invoice Amount'] = pd.to_numeric(df['Invoice Amount'], errors='coerce').fillna(0)
df = df.dropna(subset=['URN Aging'])

# 3. Features
X = df[['Invoice Amount']]
y = df['URN Aging']

# 4. Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Save
mae = mean_absolute_error(y_test, model.predict(X_test))
print(f"Model v1 MAE: {mae:.2f} days")
joblib.dump(model, 'invoice_model_v1.pkl')