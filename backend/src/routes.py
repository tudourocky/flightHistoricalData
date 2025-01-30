from src import app
from flask import jsonify, request

@app.route('/')
def hello():
    return "Welcome to the Flight Price Data API!"

@app.route('/api/flights', methods=['GET'])
def get_flights():
    date = request.args.get('date')
    start = request.args.get('start')
    end = request.args.get('end')
    trip = request.args.get('trip')
    seat = request.args.get('seat')
    adult = request.args.get('adult')
    child = request.args.get('child')
    infant = request.args.get('infant')
    infants_lap = request.args.get('infants_lap')

    result = utils.load_flights(date, start, end, trip, seat, adult, child, infant, infants_lap)

    for flight in result:
        print(flight)

    return jsonify(result)


from src import utils