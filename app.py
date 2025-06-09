from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return 'OK', 200

@app.route('/uppercase', methods=['POST'])
def uppercase():
    data = request.get_json()
    if not data or 'payload' not in data:
        return jsonify({'error': 'Missing payload field'}), 400
    
    payload = data['payload']
    if not isinstance(payload, str):
        return jsonify({'error': 'Payload must be a string'}), 400
    
    return jsonify({'data': payload.upper()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    