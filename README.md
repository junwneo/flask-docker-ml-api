# DSS5105 Data Science Projects in Practice
Exercise 2

## Running the API Test in Codespaces (via Docker)

To run the API test, follow these steps to set up Docker in your Codespace environment:

```bash
docker build -t my-api .
docker run -p 5000:5000 my-api
```

Once the container is running, you can test the API using `curl`:

Test the API with the following input values:
```bash
curl "http://localhost:5000/predict_engagement?W=1&X=20"
```
