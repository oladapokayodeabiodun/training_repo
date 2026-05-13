from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "Training@1089"


@app.route('/')
def home():
    return "Training Chat is Connected"


@app.route('/webhook', methods=['GET'])
def verify_webhook():
    
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403

    return "Welcome Accolad Konzepts Training BOT", 200


@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.get_json()

    print("Webhook Event:")
    print(data)

    return "EVENT RECEIVED", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
