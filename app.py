from flask import Flask, request
import requests 
import os 

app = Flask(__name__)

#VERIFY_TOKEN = "Training@1089"

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")
WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID")


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

    try:
        entry = data["entry"][0]
        changes = entry["changes"][0] 
        value = changes["value"]

        if "messages" in value:
            message = value["messages"][0]
            from_number = message["from"]
            text = message["text"]["body"]
            print(f"Learning from {from_number}: {text}")

            send_whatsapp_message(
                from_number,
                f"Sender asked: {text}"
            )
    except Exception as e:
        print("Not working:", e)
    
    return "EVENT RECEIVED", 200

def send_whatsapp_message(to, text):
    url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorisation": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product: "whatsapp",
        "to": to,
        "text": {
            "body": text
        }
    }

    response = request.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.text)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
