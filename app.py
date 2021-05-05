#Create dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Set Up the Database
engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()

#Reflect Tables in Database
Base.prepare(engine, reflect=True)

#Save References to Each Table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create a Session Link from Python to the Database
session = Session(engine)

#Set Up Flask - Create a New Flask App Instance
app = Flask(__name__)

#All Routes Should Go AFTER the app = FLASK(__name__)
#Create Flask Routes. The first one is the 'welcome' route
@app.route('/')

#Create welcome() function. When creating routes, follow the 
# naming convention /api/v1.0/ followedc by the name of the routh.
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#Create precipitation routh
@app.route('/api/v1.0/precipitation')

#Create precipitation function
def precipitation():
    prev_year = dt.datetime(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
