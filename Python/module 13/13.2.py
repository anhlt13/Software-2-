import mysql, json
import mysql.connector
from flask import Flask, Response

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game2',
         user='root',
         password='06042004',
         autocommit=True
         )
app = Flask(__name__)
@app.route('/airport/<icao>')
def airport(icao):
    try:
        icao_sql =f"SELECT NAME, MUNICIPALITY FROM AIRPORT WHERE IDENT='{icao}'"
        icao_cursor = connection.cursor()
        icao_cursor.execute(icao_sql)
        result = icao_cursor.fetchall()
        if icao_cursor.rowcount>0:
            for row in result:
                response = {
                    "ICAO" : icao,
                    "Name" : row[0],
                    "Location" : row[1],
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