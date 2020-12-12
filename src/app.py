#!-*-coding:utf-8-*-
import os
from dotenv import load_dotenv

load_dotenv(
    os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        'config.env'
    )
)

import logging
from flask import Flask
from flask_restx import Api
from src.rest.noticias.routes import api as noticias_api
from flask_mongoengine import MongoEngine
from src.config import (
    DB_NAME, DB_HOST, DB_USERNAME, DB_PASSWORD, DB_PORT, DB_AUTH_SOURCE
)


def config_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_namespace(noticias_api, path='/noticias')

    app.config['MONGODB_SETTINGS'] = {
        'db': DB_NAME,
        'host': DB_HOST,
        'port': DB_PORT,
        'username': DB_USERNAME,
        'password': DB_PASSWORD,
        'authentication_source': DB_AUTH_SOURCE
    }
    app.logger.setLevel(logging.INFO)
    MongoEngine(app)
    return app


app = config_app()
