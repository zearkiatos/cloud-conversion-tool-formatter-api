from flask import Flask, request, jsonify
from google.oauth2 import service_account
from googleapiclient import discovery
from config import Config

config = Config()

credentials = service_account.Credentials.from_service_account_file(
    config.GOOGLE_PUB_SUB_CREDENTIALS, scopes=['https://www.googleapis.com/auth/cloud-platform']
)

pubsub = discovery.build('pubsub', 'v1', credentials=credentials)

def receive_message(topic:str, subscription:str,projectId:str):
    subscription_path = f'projects/{projectId}/subscriptions/{subscription}'
    body = {
        'returnImmediately': True,
        'maxMessages': 1,
    }
    response = pubsub.projects().subscriptions().pull(
        subscription=subscription_path, body=body
    ).execute()

    if 'receivedMessages' in response:
        message = response['receivedMessages'][0]
        data = message['message']['data']
        ack_id = message['ackId']

        # Acknowledge the received message
        pubsub.projects().subscriptions().acknowledge(
            subscription=subscription_path, body={'ackIds': [ack_id]}
        ).execute()

        return jsonify({'message': data})
    else:
        return jsonify({'message': 'No messages available'})