#!-*-coding:utf-8-*-

from flask import request
from flask_restx import Resource
from src.api.apps.noticias.domain.services import NoticiasService
from src.rest.noticias.conf import api, post_schema, update_schema


class NoticiasGetPostView(Resource):

    @api.doc(params={
        'val': {'description': 'Valor para pesquisa da notícia'},
    })
    def get(self) -> dict:
        return NoticiasService().search_by(request.args.get("val", None))

    @api.expect(post_schema)
    def post(self):
        return NoticiasService().create(
            request.get_json()
        )


class NoticiasPutDeleteView(Resource):

    @api.expect(update_schema)
    def put(self, noticia_id: str):
        data = request.get_json()
        data['id'] = noticia_id
        return NoticiasService().update(data)

    def delete(self, noticia_id: str):
        NoticiasService().delete(noticia_id)
        return {}, 200
