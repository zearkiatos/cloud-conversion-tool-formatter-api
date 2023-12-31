
from .views import HealthCheckView, ConvertView
from flask_restful import Resource, Api
from flask import Flask, request, json
from flask_middleware_jwt import Middleware
import requests
from flaskr import create_app
from config import Config
from celery import Celery
from .dataContext.sqlAlchemyContext import db
from .jobs.consumers import start_consuming

config = Config()


app = create_app('default')

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
#resources
api.add_resource(HealthCheckView, '/health')
api.add_resource(ConvertView, '/pubsub/receive')