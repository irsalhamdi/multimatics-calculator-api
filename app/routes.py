from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Welcome to Calculator API!'

@main.route('/add')
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({'result': a + b})
