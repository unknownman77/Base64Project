from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode_text():
    data = request.get_json()
    text_to_encode = data.get('text', '')

    if not text_to_encode:
        return jsonify({'error': 'No text provided for encoding'}), 400

    try:
        encoded_bytes = base64.b64encode(text_to_encode.encode('utf-8'))
        encoded_string = encoded_bytes.decode('utf-8')
        return jsonify({'result': encoded_string})
    except Exception as e:
        return jsonify({'error': f'Encoding failed: {str(e)}'}), 500

@app.route('/decode', methods=['POST'])
def decode_text():
    data = request.get_json()
    text_to_decode = data.get('text', '')

    if not text_to_decode:
        return jsonify({'error': 'No text provided for decoding'}), 400

    try:
        decoded_bytes = base64.b64decode(text_to_decode)
        decoded_string = decoded_bytes.decode('utf-8')
        return jsonify({'result': decoded_string})
    except Exception as e:
        return jsonify({'error': f'Decoding failed. Ensure it is valid Base64: {str(e)}'}), 400
