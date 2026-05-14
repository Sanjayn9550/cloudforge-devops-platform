from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to CloudForge DevOps Platform!"

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "application": "CloudForge",
        "version": "1.0"
    })

@app.route('/about')
def about():
    return jsonify({
        "project": "CloudForge DevOps Platform",
        "technology": [
            "Flask",
            "Docker",
            "Kubernetes",
            "Jenkins",
            "Prometheus",
            "Grafana",
            "AWS"
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
