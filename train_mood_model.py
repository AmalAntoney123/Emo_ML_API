import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the data
data = pd.read_csv('mood_data.csv')

# Prepare the features and target
features = ['sleep_quality', 'stress_level', 'physical_activity', 'day_of_week']
X = data[features].copy()  # Create an explicit copy
y = data['mood']

# Add cyclical encoding for day of week
X['day_sin'] = np.sin(2 * np.pi * X['day_of_week'] / 7)
X['day_cos'] = np.cos(2 * np.pi * X['day_of_week'] / 7)
X = X.drop('day_of_week', axis=1)


# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the model
model = MLPRegressor(hidden_layer_sizes=(10, 5), max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred = model.predict(X_test_scaled)
test_mae = mean_absolute_error(y_test, y_pred)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred))
test_r2 = r2_score(y_test, y_pred)

print(f"Test MAE: {test_mae:.2f}")
print(f"Test RMSE: {test_rmse:.2f}")
print(f"Test R² Score: {test_r2:.2f}")

# Calculate baseline MAE (always predicting mean)
baseline_pred = np.full_like(y_test, y_train.mean())
baseline_mae = mean_absolute_error(y_test, baseline_pred)
print(f"Baseline MAE: {baseline_mae:.2f}")

# Save the model and scaler
with open('mood_model.pkl', 'wb') as f:
    pickle.dump((model, scaler), f)

print("Model saved successfully.")
