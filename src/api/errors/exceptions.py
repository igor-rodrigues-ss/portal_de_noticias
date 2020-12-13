#!-*-coding:utf-8-*-

from werkzeug.exceptions import BadRequest
from src.api.errors.codes import (
    FIELD_NOT_SHOULD_HAS_INT_VALUE, FIELD_IS_REQUIRED,
    INVALID_NOTICIA_ID, INVALID_STRUCTURE
)
from src.log import log


class FieldNotShouldHasNumbers(BadRequest):

    def __init__(self, *args, **kwargs):
        MSG = f"O campo '{args[0]}' não deve possuir valores numéricos."
        self.data = {
            'detail': MSG,
            'code': FIELD_NOT_SHOULD_HAS_INT_VALUE,
        }
        log.error(MSG)
        super().__init__(*args, **kwargs)


class FieldIsRequired(BadRequest):

    def __init__(self, *args, **kwargs):
        MSG = f"O campo '{args[0]}' é obrigatório."
        self.data = {
            'detail': MSG,
            'code': FIELD_IS_REQUIRED,
        }
        log.error(MSG)
        super().__init__(*args, **kwargs)


class InvalidNoticiaID(BadRequest):

    def __init__(self, *args, **kwargs):
        MSG = f"O valor '{args[0]}' é um ID inválido."
        self.data = {
            'detail': MSG,
            'code': INVALID_NOTICIA_ID,
        }
        log.error(MSG)
        super().__init__(*args, **kwargs)


class InvalidStucture(BadRequest):

    def __init__(self, *args, **kwargs):
        MSG = "Os dados enviados possuem um estrutura inválida. " \
            "Os campos esperados são: 'titulo', 'texto' e 'auto.nome'."
        self.data = {
            'detail': MSG,
            'code': INVALID_STRUCTURE,
        }
        log.error(MSG)
        super().__init__(*args, **kwargs)
