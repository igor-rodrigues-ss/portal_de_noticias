#!-*-coding:utf-8-*-

import os


DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = int(os.environ.get('DB_PORT'))
DB_USERNAME = os.environ.get('DB_USERNAME', '')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_AUTH_SOURCE = os.environ.get('DB_AUTH_SOURCE', '')
FLASK_LOGGER_NAME = 'src.app'

NoneType = type(None)
