import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# Load your housing price dataset (replace 'your_dataset.csv' with your actual dataset file)
data = pd.read_csv('housing.csv')

# Assume 'price' is the column representing housing prices
X = data[['feature1', 'feature2', 'feature3', ...]]  # Include relevant features
y = data['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the Isolation Forest model
clf = IsolationForest(contamination=0.05, random_state=42)
clf.fit(X_train_scaled)

# Predict on the test set
y_pred = clf.predict(X_test_scaled)

# Evaluate the model
print(classification_report(y_test, y_pred))
