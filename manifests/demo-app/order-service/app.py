import logging
import os
import requests
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
app = Flask(__name__)

PAYMENT_SERVICE_URL = os.getenv("PAYMENT_SERVICE_URL", "http://payment-service:5000")

@app.route("/health", methods=["GET"])
def health():
    app.logger.info("Handling request to order-service health check")
    return jsonify({"service": "order-service", "status": "ok"})

@app.route("/orders", methods=["GET", "POST"])
def create_order():
    app.logger.info("Creating order #1001, contacting payment-service...")
    try:
        resp = requests.post(f"{PAYMENT_SERVICE_URL}/pay", json={"amount": 99.99}, timeout=5)
        payment_res = resp.json()
    except Exception as e:
        app.logger.error(f"Error calling payment-service: {e}")
        payment_res = {"error": str(e)}
    return jsonify({"orderId": 1001, "status": "created", "payment": payment_res})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
