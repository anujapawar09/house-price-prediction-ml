import pickle

with open("../models/model.pkl", "rb") as f:
    model = pickle.load(f)

area = float(input("Enter area: "))
bedrooms = int(input("Enter bedrooms: "))

import pandas as pd

input_data = pd.DataFrame([[area, bedrooms]], columns=["area", "bedrooms"])
prediction = model.predict(input_data)

print("Predicted Price:", prediction[0])