import logging
import os
import requests
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
app = Flask(__name__)

REVIEWS_SERVICE_URL = os.getenv("REVIEWS_SERVICE_URL", "http://reviews-service:5000")

@app.route("/health", methods=["GET"])
def health():
    app.logger.info("Handling request to auth-service health check")
    return jsonify({"service": "auth-service", "status": "ok"})

@app.route("/login", methods=["GET", "POST"])
def login():
    app.logger.info("Processing auth login, fetching product reviews...")
    try:
        resp = requests.get(f"{REVIEWS_SERVICE_URL}/reviews", timeout=5)
        reviews_data = resp.json()
    except Exception as e:
        app.logger.error(f"Error fetching reviews: {e}")
        reviews_data = {"error": str(e)}
    return jsonify({"user": "demo-user", "auth": "authenticated", "reviews": reviews_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
