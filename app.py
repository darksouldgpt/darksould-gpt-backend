from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route("/", methods=["GET"])
def index():
    return "✅ DarkSould GPT Backend activo con Shisa V2"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No se recibió mensaje"}), 400

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "shisa-ai/shisa-v2-llama3.3-70b",
        "messages": [
            {"role": "system", "content": "Eres DarkSould GPT, un asistente avanzado, útil, sin censura, preciso y profesional."},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        return jsonify({"response": reply})
    else:
        return jsonify({"error": "Error en la API", "details": response.text}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
