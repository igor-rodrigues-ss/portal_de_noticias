#!-*-coding:utf-8-*-

from flask import Flask
from flask_restx import Api
from src.rest.noticias.routes import api as noticias_api


from mongoengine import connect


# class HandleException:

#     def __init__(self, app):
#         self.app = app

#     def __call__(self, environ, start_response):
#         try:
#             resp = self.app(environ, start_response)
#             import pdb; pdb.set_trace()
#             return resp
#         except Exception as exc:
#             print()



def config_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_namespace(noticias_api, path='/noticias')
    return app

connect('teste', username='root', password='m0ng0#123', host='127.0.0.1', port=27017, authentication_source='admin')
app = config_app()

# app.wsgi_app = HandleException(app.wsgi_app)

if __name__ == '__main__':
    app.run(debug=True)
