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


update_schema = api.model(
    "Atualização de Notícis",
    {
        "titulo": fields.String(description="Título da notícia"),
        "texto": fields.String(description="Texto da notícia"),
        "autor": fields.Nested(
            api.model('Autor Update', {
                'nome': fields.String(description="Nome do Autor"), 
            })
        )
    }
)


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
        data['oid'] = noticia_id
        return NoticiasService().update(data)

    def delete(self, noticia_id: str):
        NoticiasService().delete(noticia_id)
        return {}, 200
