#!-*-coding:utf-8-*-

from src.rest.noticias.views import (
    NoticiasGetPostView, NoticiasPutDeleteView, api
)


api.add_resource(
    NoticiasGetPostView, '/', endpoint='noticias_get_post'
)
api.add_resource(
    NoticiasPutDeleteView, '/<string:noticia_id>', endpoint='noticias_put_delete'
)
