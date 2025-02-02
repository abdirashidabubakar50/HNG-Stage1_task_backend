from flask import Flask, jsonify, Blueprint, request
import datetime
from flask_cors import CORS
from utils.helpers import is_prime, is_armstrong, is_even_or_odd, is_perfect, sum_digits


app = Flask(__name__)
CORS(app)

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/classify-number', methods=['GET'])
def math_fun_fact():
    """ get the number from the url """
    try:
        number = int(request.args.get('number'))
    except (TypeError, ValueError):
        return jsonify({
            'number': "alphabet",
            'error': True
        }), 400
    prime = is_prime(number)
    perfect = is_perfect(number)
    even_or_odd = is_even_or_odd(number)
    armstrong = is_armstrong(number)
    digit_sum = sum_digits(number)

    properties = []
    if armstrong:
        properties.append("armstrong")
    properties.append(even_or_odd)


    fun_fact = "This number does not have a fun fact"
    if armstrong:
        digits = [int(d) for d in str(number)]
        cubes = [f"{digit}^{len(digits)}" for digit in digits]
        fun_fact = f"{number} is an Armstrong number because {' + '. join(cubes)} = {number}"

    return jsonify({
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit-sum": digit_sum,
        "fun_fact": fun_fact
    }), 200

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)