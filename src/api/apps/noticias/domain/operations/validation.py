#!-*-coding:utf-8-*-

import re
from src.api.apps.noticias.domain.entities.noticia import Noticia
from src.api.errors.exceptions import StrNotShouldHasIntValues


class Validation:

    _noticia: Noticia

    def __init__(self, noticia: Noticia):
        self._noticia = noticia

    def _str_has_number(self, txt: str):
        if txt is not None:
            return bool(re.search(r'\d+', txt))

    def validate(self):
        if self._str_has_number(self._noticia.autor.nome):
            raise StrNotShouldHasIntValues('autor.nome')
