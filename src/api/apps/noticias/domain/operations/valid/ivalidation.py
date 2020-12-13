#!-*-coding:utf-8-*-

import re
from src.api.errors.exceptions import (
    StrNotShouldHasIntValues, FieldIsRequired
)
from abc import ABC, abstractmethod


class IValidation(ABC):

    def _str_has_number(self, txt: str):
        if txt is not None:
            return bool(re.search(r'\d+', txt))

    def _autor_nome_should_be_str(self, data: dict):
        if self._str_has_number(data['autor']['nome']):
            raise StrNotShouldHasIntValues('autor.nome')

    def _field_is_required(self, data: dict, field_name: str):
        oid = data.get(field_name, None)
        if oid is None or oid == '':
            raise FieldIsRequired(field_name)

    @abstractmethod
    def validate(self):
        pass
