import datetime


import os
from celery import Celery
from celery.signals import task_postrun
from flask.globals import current_app
from config.config import Config
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
import logging
from ..converters.converters import Converter
from ..models.conversion import Conversion
from ..dataContext.sqlAlchemyContext import db

config = Config()
converter=Converter()


celery_app = Celery('tasks', broker=f'{config.REDIS_BROKER_BASE_URL}/0')

TASK_POSTED, = config.TASK_POSTED_TOPICS


@celery_app.task(name=TASK_POSTED)
def convert_video(task_json):
    print(task_json)
    input_file=config.PATH_STORAGE+'input/'+task_json['id']+task_json['fileName']
    extension = os.path.splitext(input_file)[1]
    print(task_json['newFormat'])
    print(extension.upper())
    if(task_json['newFormat']=='MP4' and extension.upper().replace('.','')=='AVI'):
        converter.avitomp4(input_file,task_json['fileName'])
    else:
        print('no supported')

    #changing status in database
    conversion=Conversion.query.filter_by(id=int(task_json['id'])).one()
    conversion.status='processed'
    db.session.commit()

    print('video converted success')
    



@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()


