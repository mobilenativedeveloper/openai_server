from utils import utils
from datetime import datetime
from flask import Flask, request, jsonify
from ai import ai
app = Flask(__name__)

@app.route("/message", methods=["POST"])
@utils.catch
def message():
    try:
        engine = request.values["engine"]
    except:
        engine = "davinci"

    try:
        temperature = request.values["temperature"]
    except:
        temperature = 0.9

    try:
        max_tokens = request.values["max_tokens"]
    except:
        max_tokens = 150

    try:
        top_p = request.values["top_p"]
    except:
        top_p = 1

    try:
        presence_penalty = request.values["presence_penalty"]
    except:
        presence_penalty = 0.6

    try:
        message = request.values["message"]
    except:
        return jsonify(
            status=400,
            errorMessage="Parameter message is required."
        )
    answer = ai.ask(message, engine, temperature, max_tokens, top_p, presence_penalty)
    return jsonify(
        sender_message=str(message),
        answer=str(answer),
        timestamp=datetime.timestamp(datetime.now()),
        openai_properties={
            "engine": engine,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "presence_penalty": presence_penalty
        }
    )

@app.route("/engines", methods=["GET"])
@utils.catch
def engines():
    return jsonify(ai.engines())

if __name__ == "__main__":
    app.run(debug=True)