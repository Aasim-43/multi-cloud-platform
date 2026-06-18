import joblib

model = joblib.load("ai/failure_model.pkl")

sample = [[85, 75, 70, 90]]

prediction = model.predict(sample)

print(prediction)
