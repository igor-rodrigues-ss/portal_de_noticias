#!-*-coding:utf-8-*-


from pydantic import BaseModel
from src.config import NoneType
from typing import Union


class Autor(BaseModel):
    nome: Union[str, NoneType]
    oid: Union[str, NoneType] = None
