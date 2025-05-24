from flask import Flask, request, jsonify
from flask_cors import CORS
import pyperclip as pc
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

api = os.getenv('OPENAI_API_KEY')
if not api:
    raise ValueError("OpenAI API key not found in environment variables")

client = OpenAI(api_key=api)

@app.route('/api/generate', methods=['POST'])
def generate_response():
    try:
        data = request.get_json()
        prompt = data.get('prompt')

        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )

        generated_text = response.choices[0].message.content.strip()
        pc.copy(generated_text)
        print(generated_text)

        return jsonify({'response': generated_text, 'message': 'Copied to clipboard'}), 200

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)