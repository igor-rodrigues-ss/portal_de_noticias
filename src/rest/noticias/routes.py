#!-*-coding:utf-8-*-

from flask_restx import Namespace
from src.rest.noticias.views import (
    NoticiasGetPostView, NoticiasPutDeleteView, api
)


# api = Namespace('Noticias')

api.add_resource(
	NoticiasGetPostView, '/', endpoint='noticias_get_post'
)
api.add_resource(
	NoticiasPutDeleteView, '/<string:noticia_id>' , endpoint='noticias_put_delete'
)
