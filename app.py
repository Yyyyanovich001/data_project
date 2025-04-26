from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OPENROUTER_API_KEY = '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'
OPENROUTER_MODEL = 'icrosoft/mai-ds-r1:free'  # Example

SYSTEM_PROMPT = """
You are a Chill Mentor chatbot.
You answer with a calm, relaxed tone, giving simple but meaningful advice like a wise older friend.
Stay positive, encouraging, and human-like.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    headers = {
        'Authorization': f'Bearer {OPENROUTER_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    }
    response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json=payload)
    bot_message = response.json()['choices'][0]['message']['content']

    return jsonify({'reply': bot_message})

if __name__ == '__main__':
    app.run(debug=True)
