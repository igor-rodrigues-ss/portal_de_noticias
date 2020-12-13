#!-*-coding:utf-8-*-

import re
from src.api.errors.exceptions import (
    FieldNotShouldHasNumbers, FieldIsRequired
)
from abc import ABC, abstractmethod


class IValidation(ABC):

    def _str_has_number(self, txt: str):
        if txt is not None:
            return bool(re.search(r'\d+', txt))

    def _field_should_be_str(self, name: str, val: str):
        if self._str_has_number(val):
            raise FieldNotShouldHasNumbers(name)

    def _field_is_required(self, data: dict, field_name: str):
        val = data.get(field_name, None)
        if val is None or val == '':
            raise FieldIsRequired(field_name)

    def _validate_autor_nome(self, data: dict):
        autor_dct = data.get('autor', None)
        autor_nome = None
        if isinstance(autor_dct, dict):
            autor_nome = autor_dct.get('nome', None)
        self._field_should_be_str('autor.nome', autor_nome)

    @abstractmethod
    def validate(self):
        pass
