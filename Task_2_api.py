from flask import Flask, jsonify, request, Response
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load JSON data once
with open("Task 1 - Satpathy - Parser.json", "r") as f:
    cargo_data = json.load(f)


@app.route("/api/cargo", methods=["GET"])
def get_cargo():
    # Check header
    override = request.headers.get("X-System-Override")

    if override == "true":
        return Response("System override denied.", status="418 I'm a teapot", mimetype="text/plain")

    return jsonify(cargo_data)

if __name__ == "__main__":
    app.run(debug=True)