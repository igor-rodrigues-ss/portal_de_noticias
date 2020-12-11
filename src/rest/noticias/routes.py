#!-*-coding:utf-8-*-

from flask_restx import Namespace
from src.rest.noticias.views import (
    NoticiasGetPostView, NoticiasPutDeleteView, api
)


# api = Namespace('Noticias')

api.add_resource(NoticiasGetPostView, '/')
api.add_resource(NoticiasPutDeleteView, '/<int:noticia_id>')
