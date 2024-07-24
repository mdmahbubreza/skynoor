from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="flights"
)

@app.route('/search', methods=['POST'])
def search_flights():
    data = request.get_json()
    app.logger.debug(f'Received search request: {data}')
    origin = data['origin']
    destination = data['destination']
    departure_date = data['departureDate']

    try:
        cursor = db.cursor(dictionary=True)
        query = ("SELECT airline, price FROM flights "
                 "WHERE origin = %s AND destination = %s AND departure_date = %s")
        cursor.execute(query, (origin, destination, departure_date))
        flights = cursor.fetchall()
        cursor.close()
        app.logger.debug(f'Flights found: {flights}')
    except Exception as e:
        app.logger.error(f'Error querying database: {e}')
        return jsonify(error='Database error'), 500

    return jsonify(flights=flights)

if __name__ == '__main__':
    app.run(debug=True)
