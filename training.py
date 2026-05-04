from flask import Flask, request, jsonify

training = Flask(__name__)

@training.route("/webhook", methods=["GET", "POST"])
def webhook():
    return 'Training Chat is Connected'

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    training.run(host='0.0.0.0', port=port)

@training.route("/webhook", methods=["GET"])
def verify():
    token = "TrainingChat@1089"
    if request.args.get("hub.verify_token") == token:
        return request.args.get("hub.challenge")
    return "Invalid token"

@training.route("/webhook", methods=["POST"])
def receive_message():
    data = request.get_json()
    print(data)
    return jsonify(status="success")

#message = data["entry"][0]["changes"][0]["values"]["messages"][0]["text"]["body"]

#if message.lower() == "hello":