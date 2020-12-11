#!-*-coding:utf-8-*-

from flask import request
from flask_restx import api, Resource, Namespace
from src.api.apps.noticias.domain.services import NoticiasService
from flask_restx import fields

api = Namespace('Noticias')


post_schema = api.model(
    "Criação de Notícias", 
    {
        "titulo": fields.String(description="Título da notícia", required=True),
        "texto": fields.String(description="Texto da notícia", required=True),
        "autor": fields.Nested(
            api.model('Autor', {
                'nome': fields.String(description="Nome do Autor", required=True), 
            })
        )
    }
)


class NoticiasGetPostView(Resource):

    @api.doc(params={
        'titulo': {'description': 'Título da Notícia'},
        'texto': {'description': 'Conteúdo da Notícia'},
        'nome_do_autor': {'description': 'Nome do Autor'}
    })
    def get(self) -> dict:
        return NoticiasService().search_by()

    @api.expect(post_schema)
    def post(self):
        return NoticiasService().create(
            request.get_json()
        )


class NoticiasPutDeleteView(Resource):

    def put(self, noticia_id: int):
        return {'put': noticia_id}

    def delete(self, noticia_id: int):
        return {'delete': noticia_id}
