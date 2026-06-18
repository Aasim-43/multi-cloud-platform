import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("ai/dataset.csv")

X = data[
["cpu_usage", "memory_usage", "disk_usage", "network_usage"]
]

y = data["failure"]

model = RandomForestClassifier()

model.fit(X, y)

joblib.dump(model, "ai/failure_model.pkl")

print("Model trained and saved.")
