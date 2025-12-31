from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API is running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    number = data['number']
    result = number * 2
    return jsonify({
        "input": number,
        "output": result
    })

if __name__ == '__main__':
    app.run(debug=True)
