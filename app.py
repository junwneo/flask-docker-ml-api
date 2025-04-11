from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Training data
data = pd.DataFrame({
    "Y": [137, 118, 124, 124, 120, 129, 122, 142, 128, 114,
          132, 130, 130, 112, 132, 117, 134, 132, 121, 128],
    "W": [0, 1, 1, 1, 0, 1, 1, 0, 0, 1,
          1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    "X": [19.8, 23.4, 27.7, 24.6, 21.5, 25.1, 22.4, 29.3, 20.8, 20.2,
          27.3, 24.5, 22.9, 18.4, 24.2, 21.0, 25.9, 23.2, 21.6, 22.8]
})

# Fit linear regression model: Y = α + τ·W + β·X + ε
X_features = data[["W", "X"]]
y_outcome = data["Y"]
reg = LinearRegression().fit(X_features, y_outcome)

intercept = reg.intercept_
tau = reg.coef_[0] # Treatment effect (ATE)
beta = reg.coef_[1] # Spending coefficient

@app.route("/predict")
def predict():
    return jsonify({
        "intercept (α)": round(intercept, 3),
        "ATE (τ)": round(tau, 3),
        "Beta (β)": round(beta, 3)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
