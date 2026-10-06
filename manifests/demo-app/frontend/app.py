import logging
import os
import requests
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
app = Flask(__name__)

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:5000")

@app.route("/", methods=["GET"])
@app.route("/health", methods=["GET"])
def health():
    app.logger.info("Handling request to frontend health check")
    return jsonify({"service": "frontend", "status": "ok"})

@app.route("/login", methods=["GET", "POST"])
def login():
    app.logger.info("Frontend received login request, calling auth-service...")
    try:
        resp = requests.get(f"{AUTH_SERVICE_URL}/login", timeout=5)
        return jsonify({"frontend": "ok", "auth_response": resp.json()})
    except Exception as e:
        app.logger.error(f"Error calling auth-service: {e}")
        return jsonify({"frontend": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
