from flask import Flask
from celery import Celery
from config.config import Config

config = Config()
celery = Celery(__name__, broker=f'{config.REDIS_BROKER_BASE_URL}/0')  



def create_app(config_name):
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI']=config.DATA_BASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['PROPAGATE_EXCEPTIONS']=True
    return app

from .app import *