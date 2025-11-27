from flask import Flask, jsonify, request
from ai_module import simple_ai_reply

app = Flask(__name__)

@app.route("/")
def index():
    return "<h3>Servicio Flask IA - coello v1.0.5</h3>"

@app.route("/api/ai", methods=["POST"])
def ai():
    payload = request.json or {}
    prompt = payload.get("prompt", "")
    reply = simple_ai_reply(prompt)
    return jsonify({"prompt": prompt, "reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
