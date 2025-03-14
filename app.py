from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# DeepSeek API Key (Directly in Code)
DEEPSEEK_API_KEY = "your-deepseek-api-key"
DEEPSEEK_URL = "https://api.deepseek.com/generate"  # Replace with actual API URL

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    payload = {
        "model": "deepseek-model-name",  # Replace with actual model name
        "prompt": prompt,
        "max_tokens": 100
    }
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}

    response = requests.post(DEEPSEEK_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to get response"+prompt}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)