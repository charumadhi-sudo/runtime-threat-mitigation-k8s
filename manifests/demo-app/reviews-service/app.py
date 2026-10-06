import logging
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    app.logger.info("Handling request to reviews-service health check")
    return jsonify({"service": "reviews-service", "status": "ok"})

@app.route("/reviews", methods=["GET"])
def get_reviews():
    app.logger.info("Serving reviews list")
    return jsonify({
        "reviews": [
            {"id": 1, "product": "K8s Security Book", "rating": 5, "comment": "Great runtime security guide!"},
            {"id": 2, "product": "eBPF Handbook", "rating": 5, "comment": "Essential Falco reference."}
        ]
    })

# Designated vulnerable entry point for attack simulation
@app.route("/api/upload", methods=["POST", "GET"])
def upload():
    filename = request.form.get("filename", "unknown.dat")
    app.logger.info(f"[REVIEWS-SERVICE] Upload file received: {filename}")
    return jsonify({"status": "uploaded", "filename": filename})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
