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
from google.cloud import storage
import tempfile

config = Config()
converter=Converter()


celery_app = Celery('tasks', broker=f'{config.REDIS_BROKER_BASE_URL}/0')

TASK_POSTED, = config.TASK_POSTED_TOPICS


@celery_app.task(name=TASK_POSTED)
def convert_video(task_json):
    print(task_json)
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(config.CONVERSION_BUCKET)
    converted=True                
    print('descargando archivo del google cloud storage')
    input_file='input/'+task_json['id']+task_json['fileName']
    blob = bucket.blob(input_file)

    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        blob.download_to_filename(temp_file.name)
        input_file=temp_file.name
        idvideo=task_json['id']
        
        extension = os.path.splitext(task_json['fileName'])[1]
        destination=task_json['newFormat']
        origin=extension.upper().replace('.','')
        outputFileName=task_json['fileName']

        #MP4	WEBM	AVI	MPEG	WMV

        status='processed'
        print(f'origin= {origin}  destination={destination} tempfile={temp_file.name}')
        if(origin=='MP4' and destination=='WEBM'):
            converter.mp4towebm(idvideo,input_file,outputFileName)
            
        elif(origin=='MP4' and destination=='AVI'):
            converter.mp4toavi(idvideo,input_file,outputFileName)
        elif(origin=='MP4' and destination=='MPEG'):
            converter.mp4tompeg(idvideo,input_file,outputFileName)
        elif(origin=='MP4' and destination=='WMV'):
            converter.mp4towmv(idvideo,input_file,outputFileName)
        elif(origin=='WEBM' and destination=='MP4'):
            converter.webmtomp4(idvideo,input_file,outputFileName)
        elif(origin=='WEBM' and destination=='AVI'):
            converter.webmtoavi(idvideo,input_file,outputFileName)
        elif(origin=='WEBM' and destination=='MPEG'):
            converter.webmtompeg(idvideo,input_file,outputFileName)
        elif(origin=='WEBM' and destination=='WMV'):
            converter.webmtowmv(idvideo,input_file,outputFileName)
        elif(origin=='AVI' and destination=='MP4'):
            converter.avitomp4(idvideo,input_file,outputFileName)
        elif(origin=='AVI' and destination=='WEBM'):
            converter.avitowebm(idvideo,input_file,outputFileName)
        elif(origin=='AVI' and destination=='MPEG'):
            converter.avitompeg(idvideo,input_file,outputFileName)
        elif(origin=='AVI' and destination=='WMV'):
            converter.avitowmv(idvideo,input_file,outputFileName)
        elif(origin=='MPEG' and destination=='MP4'):
            converter.mpegtomp4(idvideo,input_file,outputFileName)
        elif(origin=='MPEG' and destination=='WEBM'):
            converter.mpegtowebm(idvideo,input_file,outputFileName)
        elif(origin=='MPEG' and destination=='AVI'):
            converter.mpegtoavi(idvideo,input_file,outputFileName)
        elif(origin=='MPEG' and destination=='WMV'):
            converter.mpegtowmv(idvideo,input_file,outputFileName)
        elif(origin=='WMV' and destination=='MP4'):
            converter.wmvmtomp4(idvideo,input_file,outputFileName)
        elif(origin=='WMV' and destination=='WEBM'):
            converter.wmvtowebm(idvideo,input_file,outputFileName)
        elif(origin=='WMV' and destination=='AVI'):
            converter.wmvmtoavi(idvideo,input_file,outputFileName)
        elif(origin=='WMV' and destination=='MPEG'):
            converter.wmvtompeg(idvideo,input_file,outputFileName)
        else:
            print('Conversion no supported')
            status='Conversion no supported'
            converted=False
            
        if converted:
            #changing status in database
            conversion=Conversion.query.filter_by(id=int(task_json['id'])).one()
            conversion.status=status
            db.session.commit()

            print('video converted success')
        else:
            print('video no converted')
    



@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()



