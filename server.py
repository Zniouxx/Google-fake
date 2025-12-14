from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows frontend (any port) to connect

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    print("Received data from frontend:")
    print("Email:", email)
    print("Password (demo):", password)
    return jsonify({
        "status": "success",
        "message": "Data received successfully!"
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
# change this ur port mine is 5000 maybe urs is 5500 or 3000
