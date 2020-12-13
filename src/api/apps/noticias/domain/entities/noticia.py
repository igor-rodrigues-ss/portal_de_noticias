#!-*-coding:utf-8-*-

from pydantic import BaseModel
from src.api.apps.noticias.domain.entities.autor import Autor
from typing import Union
from src.config import NoneType


class Noticia(BaseModel):
    titulo: Union[str, NoneType]
    texto: Union[str, NoneType]
    autor: Union[Autor, NoneType]
    oid: str = None
