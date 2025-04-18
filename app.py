from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/mojastrona')
def mojastrona():
    return "To jest moja strona!"

@app.route('/hello')
def hello():
    name = request.args.get('name')
    return f"Hello, {name}!"

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        x1 = float(request.args.get('x1', 0))
        x2 = float(request.args.get('x2', 0))
    except ValueError:
        return jsonify({'error': 'Nieprawidłowe dane wejściowe'}), 400

    result = 1 if (x1 + x2) > 5.8 else 0
    return jsonify({'x1': x1, 'x2': x2, 'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
