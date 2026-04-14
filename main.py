from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Hello from Flask!</h1>
    <p>This is a small web app for Nexus practice.</p>
    <p>Try also: <a href="/health">/health</a></p>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "app": "flask-nexus-practice"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
