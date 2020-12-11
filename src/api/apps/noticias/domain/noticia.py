#!-*-coding:utf-8-*-

from dataclasses import dataclass


@dataclass(frozen=True)
class Autor:
    nome: str


@dataclass(frozen=True)
class Noticia:
    titulo: str
    texto: str
    autor: Autor
