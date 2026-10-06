import logging
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    app.logger.info("Handling request to payment-service health check")
    return jsonify({"service": "payment-service", "status": "ok"})

@app.route("/pay", methods=["POST", "GET"])
def pay():
    app.logger.info("Processing payment transaction")
    return jsonify({"paymentId": "PAY-9988-CONFIRMED", "status": "approved", "amount": 99.99})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
