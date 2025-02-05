from flask import Flask, jsonify, Blueprint, request
import datetime
from flask_cors import CORS
from utils.helpers import is_prime, is_armstrong, is_even_or_odd, is_perfect, sum_digits, get_number_fact


app = Flask(__name__)
CORS(app)

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/classify-number', methods=['GET'])
def math_fun_fact():
    """ get the number from the url """
    number = request.args.get('number')
    try:
        number = int(number)
    except (TypeError, ValueError):
        alphabet = request.args.get('number')
        return jsonify({
            'number': alphabet,
            'error': True
        }), 400

    abs_number = abs(number)
    prime = is_prime(abs_number)
    perfect = is_perfect(abs_number)
    even_or_odd = is_even_or_odd(abs_number)
    armstrong = is_armstrong(abs_number)
    digit_sum = sum_digits(abs_number)

    properties = []
    if armstrong:
        properties.append("armstrong")
    properties.append(even_or_odd)

    fun_fact = get_number_fact(abs_number)

    return jsonify({
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }), 200

app.register_blueprint(api)

if __name__ == "__main__":
    app.run()