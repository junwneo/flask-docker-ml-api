# DSS5105 Data Science Projects in Practice
Exercise 2

## 🧠 ATE Regression API with Flask & Docker

This project implements a causal inference model to estimate the Average Treatment Effect (ATE) of a carbon offset program on stakeholder engagement. It exposes the model as a RESTful API using Flask, containerized via Docker, and is fully compatible with GitHub Codespaces.

---

## 📄 View the Report

You can view the answers to the assignment in either of the following formats:

- [📥 Download the Word version (ATE_Assignment_Answers.docx)](./ATE_Assignment_Answers.docx) - Click the link to open the file preview, then click the **"Download"** button in the upper right corner to save a local copy.
- [📄 View the Markdown version (answer.md)](./answer.md)

---

### 🚀 Features

- Linear regression estimating ATE from simulated corporate data
- Flask API exposing prediction and ATE endpoints
- Dockerized environment for full reproducibility
- JSON input/output for easy integration
- Codespaces-ready: no local setup required

---
## 📦 Project Structure & Components

* app.py – Hosts a Flask API that loads a trained regression model and predicts stakeholder engagement scores based on input treatment (W) and sustainability spending (X).

* Dockerfile – Defines the containerized environment including the base Python image, dependencies installation, and Flask app execution setup.

* requirements.txt – Lists all necessary Python libraries such as Flask, pandas, and statsmodels for the API to run.

* Containerization – Ensures the application runs consistently across different systems and simplifies deployment, collaboration, and reproducibility.

* GitHub Codespaces – Provides a cloud-based development environment pre-configured with Docker, eliminating local setup issues.

---
## 📁 Getting Started

### Running the API Test in Codespaces (via Docker)

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
