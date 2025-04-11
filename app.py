from flask import Flask, request, jsonify
import pandas as pd
import statsmodels.api as sm

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

# Fit regression model using statsmodels
X_model = sm.add_constant(data[["W", "X"]])
y_model = data["Y"]
model = sm.OLS(y_model, X_model).fit()

# Extract coefficients
intercept = model.params["const"]
tau = model.params["W"]
beta = model.params["X"]

# --- Route to estimate ATE and coefficients (Qn 1) ---
@app.route("/estimate_ate")
def estimate_ate():
    return jsonify({
        "intercept (α)": round(intercept, 3),
        "ATE (τ)": round(tau, 3),
        "Beta (β)": round(beta, 3)
    })

# --- Route to predict stakeholder engagement based on W and X (Qn 2) ---
@app.route("/predict_engagement", methods=["GET"])
def predict_engagement():
    try:
        Wi = float(request.args.get("W"))
        Xi = float(request.args.get("X"))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing input parameters W and X"}), 400

    input_df = pd.DataFrame({"const": [1], "W": [Wi], "X": [Xi]})
    pred_y = model.predict(input_df)[0]

    return jsonify({
        "W (treatment)": Wi,
        "X (spending in $1,000s)": Xi,
        "predicted engagement score (Ŷi)": round(pred_y, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
