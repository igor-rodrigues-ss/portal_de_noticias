#!-*-coding:utf-8-*-

from flask_restx import Namespace
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
    "Atualização de Notícias",
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
