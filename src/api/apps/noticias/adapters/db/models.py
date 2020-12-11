#!-*-coding:utf-8-*-

from mongoengine import *


class Autor(Document):
    nome = StringField(max_length=512)


class Noticias(Document):
    titulo = StringField(max_length=512, required=True)
    texto = StringField(required=True)
    autor = ReferenceField(
        Autor, reverse_delete_rule=CASCADE, required=True
    )
