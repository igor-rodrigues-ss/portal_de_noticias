#!-*-coding:utf-8-*-

from src.api.apps.noticias.domain.inoticias_repository import (
    INoticiasRepository
)
from src.api.apps.noticias.adapters.db.noticias_repository import (
    NoticiasRepository
)
from typing import List
from src.api.apps.noticias.domain.noticia import Noticia, Autor


class NoticiasService:

    _noticias_repo: INoticiasRepository

    def __init__(
        self, noticias_repository: INoticiasRepository = NoticiasRepository()
    ):
        self._noticias_repo = noticias_repository

    def search_by(self, data: dict = {}) -> List[dict]:
        return self._noticias_repo.search_by(None)

    def create(self, data: dict) -> dict:
        autor = Autor(nome=data['autor']['nome'])
        noticia = Noticia(
            titulo=data['titulo'], texto=data['texto'], autor=autor
        )
        return self._noticias_repo.create(noticia)
