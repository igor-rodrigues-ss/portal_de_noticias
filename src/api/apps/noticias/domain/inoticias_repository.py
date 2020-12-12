#!-*-coding:utf-8-*-

from typing import List
from abc import ABC, abstractclassmethod
from src.api.apps.noticias.domain.entities.noticia import Noticia


class INoticiasRepository(ABC):

    @abstractclassmethod
    def create(self, noticia: Noticia) -> dict:
        pass

    @abstractclassmethod
    def update(self, noticia: Noticia) -> dict:
        pass

    @abstractclassmethod
    def delete(self, noticia_id: str):
        pass

    @abstractclassmethod
    def search_by(self, value: str) -> List[dict]:
        pass
