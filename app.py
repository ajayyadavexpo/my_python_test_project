# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.json
    if 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Missing parameters'}), 400
    a = data['a']
    b = data['b']
    return jsonify({'result': a + b})

if __name__ == '__main__':
    app.run(debug=True)
