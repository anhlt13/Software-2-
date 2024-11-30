import json

from flask import Flask, request, Response
from sympy.solvers.diophantine.diophantine import divisible

app = Flask(__name__)
@app.route('/prime_number/<number>')
def check_number(number):
    try:
        number = int(number)
        divisible= 0
        for num in range(1, number + 1):
            if number%num==0:
                divisible+=1
        if divisible ==2:
            response = {
                "number": number,
                "is_prime": "True",
            }
        else:
            response = {
                "number": number,
                "is_prime": "False",
            }

        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=200, mimetype="application/json")
        return http_response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
        response = {
            "message": "Invalid endpoint",
            "status": 404
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=404, mimetype="application/json")
        return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
