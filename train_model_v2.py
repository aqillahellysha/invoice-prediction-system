# train_model_v2.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error
import joblib

print("--- Training Model v2 (Improved) ---")

# 1. Load Data (Added encoding fix here)
df = pd.read_csv('invoice_data.csv', encoding='ISO-8859-1')

# 2. Data Cleaning
df['Invoice Amount'] = df['Invoice Amount'].astype(str).str.replace(',', '', regex=False)
df['Invoice Amount'] = pd.to_numeric(df['Invoice Amount'], errors='coerce').fillna(0)
df = df.dropna(subset=['URN Aging'])

df['User Name'] = df['User Name'].fillna('Unknown')
df['Document Type'] = df['Document Type'].fillna('Unknown')

# 3. Features
X = df[['Invoice Amount', 'User Name', 'Document Type']]
y = df['URN Aging']

# 4. Pipeline
preprocessor = ColumnTransformer(transformers=[
    ('num', 'passthrough', ['Invoice Amount']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['User Name', 'Document Type'])
])

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=50, random_state=42))
])

# 5. Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# 6. Save
mae = mean_absolute_error(y_test, model.predict(X_test))
print(f"Model v2 MAE: {mae:.2f} days")
joblib.dump(model, 'invoice_model_v2.pkl')