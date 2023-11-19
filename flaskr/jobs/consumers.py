from flask import jsonify
import schedule
import json
import time
import base64
from ..consumers import taskConverseConsumer
from config import Config
from ..tasks.tasks import convert_video

config = Config()
AVAILABLE_MESSAGE =  "No messages available"

def consume_messages():
    result = taskConverseConsumer.receive_message(config.TASK_POSTED_TOPICS['TASK_POSTED'],config.SUBSCRIPTION_NAME, config.GOOGLE_PROJECT_ID)
    response = result.response[0].decode('utf-8')
    message = ''
    data = json.loads(response)
    message_base64 = (data['message'])
    print(message_base64)
    if not message_base64 == AVAILABLE_MESSAGE:
        message = base64.b64decode(message_base64).decode('latin1')
        print(message)
        convert_video(json.loads(message))
        

def start_consuming():
    consume_messages()
    schedule.every(1).seconds.do(consume_messages)

    while True:
        schedule.run_pending()
        time.sleep(30)