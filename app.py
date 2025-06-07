from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode_text():
    data = request.get_json() # Get JSON data from the request
    text_to_encode = data.get('text', '') # Extract 'text' key, default to empty string

    if not text_to_encode:
        return jsonify({'error': 'No text provided for encoding'}), 400

    try:
        # Encode the text to bytes, then base64 encode, then decode back to string for display
        encoded_bytes = base64.b64encode(text_to_encode.encode('utf-8'))
        encoded_string = encoded_bytes.decode('utf-8')
        return jsonify({'result': encoded_string})
    except Exception as e:
        return jsonify({'error': f'Encoding failed: {str(e)}'}), 500

@app.route('/decode', methods=['POST'])
def decode_text():
    data = request.get_json() # Get JSON data from the request
    text_to_decode = data.get('text', '') # Extract 'text' key, default to empty string

    if not text_to_decode:
        return jsonify({'error': 'No text provided for decoding'}), 400

    try:
        # Decode the base64 string to bytes, then decode bytes to original string
        decoded_bytes = base64.b64decode(text_to_decode)
        decoded_string = decoded_bytes.decode('utf-8')
        return jsonify({'result': decoded_string})
    except Exception as e:
        # Catch common errors like incorrect base64 padding
        return jsonify({'error': f'Decoding failed. Ensure it is valid Base64: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True) # debug=True is good for development, turn off in production