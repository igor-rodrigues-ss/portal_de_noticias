#!-*-coding:utf-8-*-

from src.api.apps.noticias.domain.operations.valid.ivalidation import (
    IValidation
)


class ValidationToUpdate(IValidation):

    _data: dict

    def __init__(self, data: dict):
        self._data = data

    def validate(self):
        self._field_is_required(self._data, 'id')
        self._autor_nome_should_be_str(self._data)
