from flask import Flask
from pymongo import MongoClient
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import atexit

app = Flask(__name__)
app.config['SECRET_KEY'] = "980035d268baeaa2e8e7b52322dc6a5fbdd3049d"
app.config['MONGO_URI'] = "mongodb+srv://tudourocky:xdbP5HMvrxTxNThM@flightpricedata.4ondr.mongodb.net/?retryWrites=true&w=majority&appName=FlightPriceData"
api = Api(app)
mongodb_client = MongoClient(app.config['MONGO_URI'])
db = mongodb_client.FlightPriceData
data_collection = db['external_data']

try:
    mongodb_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


from src import routes
# from src import utils
# from .utils import load_flights

# sceduler = BackgroundScheduler()
# sceduler.add_job(
#     func=load_flights(),
#     trigger='cron',
#     hour=0,
#     timezone='EST'
# )
# sceduler.start()

# atexit.register(lambda: sceduler.shutdown())