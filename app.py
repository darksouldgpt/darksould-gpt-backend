from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return 'DarkSould GPT - Backend activo'

# Ruta del chat
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Falta el prompt'}), 400

    # Petición a OpenRouter usando el modelo Shisa V2 Llama 3.3 70B
    response = requests.post(
        'https://openrouter.ai/api/v1/chat/completions',
        headers={
            'Authorization': 'Bearer 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',
            'Content-Type': 'application/json'
        },
        json={
            "model": "shisaai/shisa-llama-3.3-70b",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    if response.status_code != 200:
        return jsonify({'error': 'Error al consultar el modelo', 'detalle': response.text}), 500

    result = response.json()
    message = result['choices'][0]['message']['content']
    return jsonify({'response': message})
