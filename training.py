from flask import Flask, request, jsonify

training = Flask(__name__)

VERIFY_TOKEN = "Training@1089"

@training.route('/')
def webhook():
    return 'Training Chat is Connected'

@training.route('/webhook', methods=['GET'])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode and toke:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403 

    return "Welcome webhook", 200
        
@training.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    print("Webhook Event:")
    print(data)

    return "EVENT RECEIVED", 200
                        
if __name__ == '__main__':
    training.run(host='0.0.0.0', port=10000)

# @training.route("/webhook", methods=["GET"])
#def verify():
 #   token = "TrainingChat@1089"
#  if request.args.get("hub.verify_token") == token:
 #       return request.args.get("hub.challenge")
  #  return "Invalid token"

#@training.route("/webhook", methods=["POST"])
#def receive_message():
 #   data = request.get_json()
  #  print(data)
   # return jsonify(status="success")

#message = data["entry"][0]["changes"][0]["values"]["messages"][0]["text"]["body"]

#if message.lower() == "hello":
