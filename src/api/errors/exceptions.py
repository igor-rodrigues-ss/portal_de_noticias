#!-*-coding:utf-8-*-

from werkzeug.exceptions import BadRequest
from src.api.errors.codes import (
	STR_NOT_SHOULD_HAS_INT_VALUE, FIELD_IS_REQUIRED, INVALID_NOTICIA_ID
)
from src.log import log


class StrNotShouldHasIntValues(BadRequest):

    def __init__(self, *args, **kwargs):
        MSG = f"O campo '{args[0]}' não deve possuir valores numéricos."
        self.data = {
            'detail': MSG,
            'code': STR_NOT_SHOULD_HAS_INT_VALUE,
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
