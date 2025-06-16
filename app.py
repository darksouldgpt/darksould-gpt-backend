from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Para permitir peticiones desde el frontend (Vercel)

@app.route('/')
def home():
    return 'Backend DarkSould GPT listo'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')

    # Aquí irá la integración con Venice más adelante
    response = f"Echo: {message}"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
