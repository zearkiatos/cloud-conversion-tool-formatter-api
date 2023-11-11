import os
from dotenv import load_dotenv

environment = os.getenv('FLASK_ENV')

if environment == 'develop':
    load_dotenv(dotenv_path='.env.dev')
else:
    load_dotenv(dotenv_path='.env')


class Config:
    ENVIRONMENT = environment
    REDIS_BROKER_BASE_URL=os.getenv('REDIS_BROKER_BASE_URL')
    DATA_BASE_URI=os.getenv('DATA_BASE_URI')
    SECRET_KEY=os.getenv('SECRET_KEY')
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
    APP_NAME=os.getenv('APP_NAME')
    PATH_STORAGE=os.getenv('PATH_STORAGE')
    CONVERSION_BUCKET=os.getenv('CONVERSION_BUCKET')
    TASK_POSTED_TOPICS = {
        'TASK_POSTED': os.getenv('TOPIC_TASK_POSTED')
    }