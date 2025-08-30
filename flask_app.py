from flask import Flask, jsonify, request

app = Flask(__name__)


# Simple home route
@app.route("/")
def home():
    return "Hello from Flask Jenkins Quickstart!"


# Example API endpoint
@app.route("/api/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"})


if __name__ == "__main__":
    # Run on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
