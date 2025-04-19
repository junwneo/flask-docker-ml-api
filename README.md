# DSS5105 Data Science Projects in Practice
Exercise 2

## 🧠 ATE Regression API with Flask & Docker

This project implements a causal inference model to estimate the Average Treatment Effect (ATE) of a carbon offset program on stakeholder engagement. It exposes the model as a RESTful API using Flask, containerized via Docker, and is fully compatible with GitHub Codespaces.

---

### 🚀 Features

- Linear regression estimating ATE from simulated corporate data
- Flask API exposing prediction and ATE endpoints
- Dockerized environment for full reproducibility
- JSON input/output for easy integration
- Codespaces-ready: no local setup required

---

## Running the API Test in Codespaces (via Docker)

To run the API test, follow these steps to set up Docker in your Codespace environment:

```bash
docker build -t my-api .
docker run -p 5000:5000 my-api
```

---

## 🧪 Example API Usage
### Endpoint: `/predict`
Once the container is running, you can test the API using `curl`:

Test the API with the following input values:
```bash
curl "http://localhost:5000/predict_engagement?W=1&X=20"
```
