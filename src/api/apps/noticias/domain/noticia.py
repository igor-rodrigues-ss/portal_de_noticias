#!-*-coding:utf-8-*-

from pydantic import BaseModel


class Autor(BaseModel):
    nome: str
    oid: str = None


class Noticia(BaseModel):
    titulo: str
    texto: str
    autor: Autor
    oid: str = None
