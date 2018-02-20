from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Blogpost
from datetime import datetime
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)




# Connect to Database and create database session
engine = create_engine('sqlite:///blog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()





@app.route('/')
def index():
    ##posts = session.query(Blogpost).all()
    return render_template('index.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/issues')
def issues():
    return render_template('issues.html')


@app.route('/howToVote')
def howToVote():
    return render_template('howToVote.html')







if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
