import os
from flask import Flask, request,jsonify
from predict_using_logisticRegression import predict_LR

app = Flask("NLP")

port = os.getenv('PORT', None)


@app.route('/', methods = ['GET'])
def hello():
      return "Hello world",200
# def verify():
#     print(request.args)
#     # Xác minh webhook
#     if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
#         if not request.args.get("hub.verify_token") == verify_token:
#             return "Verification token mismatch", 403
#         return request.args["hub.challenge"], 200
#     return "Hello world", 200

@app.route('/', methods=['POST'])
def commandHandler():
    data = request.get_json()
    print(data["command"])
    res = predict_LR(data["command"])
    return jsonify(res), 200


if __name__ == "__main__":
    app.run(port, use_reloader = True, debug=True)
