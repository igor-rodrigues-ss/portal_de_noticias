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
        self._validate_autor_nome(self._data)
