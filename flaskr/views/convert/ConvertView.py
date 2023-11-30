from flask_restful import Resource
from flask import Flask, request, jsonify
import base64
import json
import requests
from http import HTTPStatus
from ...tasks.tasks import convert_video
from  config import Config

config = Config()

class ConvertView(Resource):
    def post(self):
        try:
            req_data = request.get_json()
            message_data = req_data['message']['data']

            decoded_message = base64.b64decode(message_data).decode('latin1')

            print(f"Received message: {decoded_message}")

            convert_video(json.loads(decoded_message))

            return jsonify({'success': True}), HTTPStatus.OK
        except Exception as ex:
            return {
                "message": "Some error ocurred"
            }, HTTPStatus.INTERNAL_SERVER_ERROR