#!-*-coding:utf-8-*-

from src.api.apps.noticias.domain.operations.valid.ivalidation import (
    IValidation
)
from src.api.errors.exceptions import InvalidStucture


class ValidationToCreate(IValidation):

    _data: dict

    def __init__(self, data: dict):
        self._data = data

    def _validate_data_struct(self, data: dict):
        for req_field in ['titulo', 'texto', 'autor']:

            # Validando titulo e texto
            if req_field not in list(data.keys()):
                raise InvalidStucture()

            # Validando estrutura do nome do autor
            if req_field == 'autor':
                autor = data.get('autor', None)

                if not isinstance(autor, dict):
                    raise InvalidStucture()

                if 'nome' not in list(autor.keys()):
                    raise InvalidStucture()

    def validate(self):
        self._validate_data_struct(self._data)
        self._validate_autor_nome(self._data)
