from flask import Flask, request, jsonify
from flask_cors import CORS
import pyperclip as pc
import os
from openai import OpenAI
from dotenv import load_dotenv

# Configuration
load_dotenv()
app = Flask(__name__)
CORS(app)

# Initialize OpenAI client
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OpenAI API key not found in environment variables")
client = OpenAI(api_key=api_key)


def generate_content(prompt, system_message=None):
    """Generic function to generate content from OpenAI"""
    messages = [{"role": "user", "content": prompt}]
    if system_message:
        messages.insert(0, {"role": "system", "content": system_message})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    generated_text = response.choices[0].message.content.strip()
    pc.copy(generated_text)
    print(generated_text)
    return generated_text


def handle_request(prompt, system_message=None):
    """Handle API requests with error handling"""
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        generated_text = generate_content(prompt, system_message)
        return jsonify({
            'response': generated_text,
            'message': 'Copied to clipboard'
        }), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate', methods=['POST'])
def generate_response():
    """Endpoint for general text generation"""
    data = request.get_json()
    return handle_request(data.get('prompt'))

@app.route('/api/generate-code', methods=['POST'])
def generate_code_response():
    """Endpoint for code generation"""
    data = request.get_json()
    system_msg = system_msg = """
        You are a code generator. Follow these rules:
        1. Return only raw code
        2. Never add comments
        3. Never include explanations
        4. Never use markdown formatting
        5. Maintain original code indentation
    """
    return handle_request(data.get('prompt'), system_msg)

if __name__ == '__main__':
    app.run(debug=True, port=5000)