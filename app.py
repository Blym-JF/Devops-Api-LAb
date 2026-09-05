from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(message="DevOps Docker API")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/version")
def version():
    return jsonify(
        version=os.getenv("APP_VERSION", "0.1.0"),
        environment=os.getenv("APP_ENV", "development"),
    )