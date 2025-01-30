from flask import Flask, jsonify
from pymongo import MongoClient
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from apscheduler.schedulers.background import BackgroundScheduler
from fast_flights import FlightData, Passengers, Result, get_flights
import requests
import atexit
import os

app = Flask(__name__)

client = MongoClient(os.getenv('MONGO_URI'))
db = client.FlightPriceData
data_collection = db['external_data']
api = Api(app)

def check_mongo_connection():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    
check_mongo_connection()


def fetch_and_store_data():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        response.raise_for_status()

        processed_data = process_data(response.json())
        data_collection.insert_one(processed_data)
    
    except Exception as e:
        app.logger.error(f'Error fetching data: {e}')

def process_data(data):
    return {
        'timestamp' : raw_data['time'],
    }

sceduler = BackgroundScheduler()
sceduler.add_job(
    func=fetch_and_store_data,
    trigger='cron',
    hour=0,
    timezone='EST'
)
sceduler.start()

atexit.register(lambda: sceduler.shutdown())

@app.route('/', methods=['GET'])
def hello():
    return "Welcome to the Flight Price Data API!"

@app.route('/api/data', methods=['GET'])
def get_all_data():
    """Get all stored data points"""
    data = list(data_collection.find({}, {'_id': 0}))
    return jsonify({'data': data})

@app.route('/api/data/latest', methods=['GET'])
def get_latest():
    """Get most recent data point"""
    latest = data_collection.find_one(
        sort=[('timestamp', -1)],
        projection={'_id': 0}
    )
    return jsonify(latest or {})


if __name__ == '__main__':
    app.run(debug=True)