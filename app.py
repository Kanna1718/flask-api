import os
import socket
import datetime
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")
APP_ENV = os.getenv("APP_ENV", "production")

# In-memory sample data store
items = [
    {"id": 1, "name": "ArgoCD", "description": "Declarative GitOps continuous delivery tool for Kubernetes"},
    {"id": 2, "name": "Kubernetes", "description": "Automated container orchestration system"},
    {"id": 3, "name": "Flask", "description": "Lightweight Python WSGI web application framework"}
]

@app.route("/")
def index():
    hostname = socket.gethostname()
    return render_template(
        "index.html",
        hostname=hostname,
        version=APP_VERSION,
        environment=APP_ENV
    )

@app.route("/health", methods=["GET"])
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "flask-api",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "hostname": socket.gethostname(),
        "version": APP_VERSION
    }), 200

@app.route("/api/info", methods=["GET"])
def info():
    return jsonify({
        "app_name": "Flask GitOps Demo API",
        "version": APP_VERSION,
        "environment": APP_ENV,
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()) if socket.gethostname() else "127.0.0.1",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }), 200

@app.route("/api/items", methods=["GET"])
def get_items():
    return jsonify({
        "success": True,
        "count": len(items),
        "data": items
    }), 200

@app.route("/api/items", methods=["POST"])
def add_item():
    payload = request.get_json(silent=True) or {}
    name = payload.get("name")
    description = payload.get("description", "")

    if not name:
        return jsonify({"success": False, "error": "Item 'name' is required"}), 400

    new_item = {
        "id": len(items) + 1,
        "name": name,
        "description": description
    }
    items.append(new_item)
    return jsonify({"success": True, "message": "Item added successfully", "item": new_item}), 201

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    # host 0.0.0.0 allows listening outside container/host
    app.run(host="0.0.0.0", port=port, debug=False)
