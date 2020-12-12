#!-*-coding:utf-8-*-

from pydantic import BaseModel
from src.api.apps.noticias.domain.entities.autor import Autor


class Noticia(BaseModel):
    titulo: str
    texto: str
    autor: Autor
    oid: str = None
