#!-*-coding:utf-8-*-

from typing import List
from abc import ABC, abstractclassmethod
from src.api.apps.noticias.domain.noticia import Noticia


class INoticiasRepository(ABC):

    @abstractclassmethod
    def create(self, noticia: Noticia):
        pass

    @abstractclassmethod
    def update(self, noticia: Noticia):
        pass

    @abstractclassmethod
    def delete(self, noticia: Noticia):
        pass

    @abstractclassmethod
    def search_by(self) -> List[dict]:
        pass
