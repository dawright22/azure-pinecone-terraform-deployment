import os
import re
import base64
import hvac
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure Vault client using environment variables
vault_url = os.getenv('VAULT_ADDR', 'http://127.0.0.1:8200')
vault_token = os.getenv('VAULT_TOKEN', 's.xxxxxxxx')
vault_namespace = os.getenv('VAULT_NAMESPACE', 'admin')

client = hvac.Client(url=vault_url, token=vault_token, namespace=vault_namespace)

# Ensure the client is authenticated
if not client.is_authenticated():
    raise Exception("Vault authentication failed")

# Define regex patterns
regex_patterns = [
    r'AKIA[0-9A-Z]{16}',
    r'ASIA[0-9A-Z]{16}',
    r'[A-Za-z0-9/+=]{40}',
    r'(?<=")[\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12}(?=")'
]


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    content = file.read().decode('utf-8')
    updated_content, replacements = replace_matches_with_encryption(content)
    
    output_path = 'redacted_' + file.filename
    with open(output_path, 'w') as f:
        f.write(updated_content)
    
    return jsonify({'message': 'File processed successfully', 'output_file': output_path})

def replace_matches_with_encryption(content):
    replacements = {}
    for pattern in regex_patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            if match not in replacements:
                encrypted_value = encrypt_with_vault(match)
                replacements[match] = encrypted_value
            content = content.replace(match, replacements[match])
    return content, replacements

def encrypt_with_vault(plain_text):
    # Encode the plain text as base64
    plain_text_base64 = base64.b64encode(plain_text.encode('utf-8')).decode('utf-8')
    encryption_response = client.secrets.transit.encrypt_data(
        name='orders',
        plaintext=plain_text_base64
    )
    return encryption_response['data']['ciphertext']

if __name__ == '__main__':
    app.run(debug=True)


