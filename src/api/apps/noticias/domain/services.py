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

    def search_by(self, value: str) -> List[dict]:
        return self._noticias_repo.search_by(value)

    def create(self, data: dict) -> dict:
        autor = Autor(nome=data['autor']['nome'])
        noticia = Noticia(
            titulo=data['titulo'], texto=data['texto'], autor=autor
        )
        return self._noticias_repo.create(noticia)

    def update(self, data: dict):
        autor_json = data.get('autor', None)
        autor_nome = autor_json.get('nome', None) if isinstance(autor_json, dict) else None
        autor = Autor(nome=autor_nome)
        noticia = Noticia(
            oid=data['oid'],
            titulo=data.get('titulo', None),
            texto=data.get('texto', None),
            autor=autor
        )
        return self._noticias_repo.update(noticia)

    def delete(self, noticia_id: str):
        # TODO: testar com ID inexistente
        self._noticias_repo.delete(noticia_id)
