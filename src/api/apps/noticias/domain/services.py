#!-*-coding:utf-8-*-

from src.api.apps.noticias.domain.inoticias_repository import (
    INoticiasRepository
)
from src.api.apps.noticias.adapters.db.noticias_repository import (
    NoticiasRepository
)
from typing import List
from src.api.apps.noticias.domain.operations.validation import Validation
from src.api.apps.noticias.domain.operations.factory_noticia import (
    FactoryNoticia
)


class NoticiasService:

    _noticias_repo: INoticiasRepository

    def __init__(
        self, noticias_repository: INoticiasRepository = NoticiasRepository()
    ):
        self._noticias_repo = noticias_repository

    def search_by(self, value: str) -> List[dict]:
        return self._noticias_repo.search_by(value)

    def create(self, data: str) -> dict:
        noticia = FactoryNoticia(data).with_required_fields()
        Validation(noticia).validate()
        return self._noticias_repo.create(noticia)

    def update(self, data: dict):
        noticia = FactoryNoticia(data).with_optional_fields()
        Validation(noticia).validate()
        return self._noticias_repo.update(noticia)

    def delete(self, noticia_id: str):
        # TODO: testar com ID inexistente
        self._noticias_repo.delete(noticia_id)
