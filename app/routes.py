from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Welcome to Calculator API!'

@main.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    return jsonify({'result': a + b})

@main.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    return jsonify({'result': a - b})

@main.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    return jsonify({'result': a * b})

@main.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    a = float(data.get('a', 0))
    b = float(data.get('b', 1))  # default 1 agar tidak ZeroDivisionError
    if b == 0:
        return jsonify({'message': 'Cannot divide by zero'}), 400
    return jsonify({'result': a / b})

@main.route('/modulus', methods=['POST'])
def modulus():
    data = request.get_json()
    a = float(data.get('a', 0))
    b = float(data.get('b', 1))
    if b == 0:
        return jsonify({'message': 'Cannot divide by zero'}), 400
    return jsonify({'result': a % b})

@main.route('/exponent', methods=['POST'])
def exponent():
    data = request.get_json()
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    return jsonify({'result': pow(a, b)})
