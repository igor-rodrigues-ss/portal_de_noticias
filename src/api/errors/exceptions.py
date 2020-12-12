#!-*-coding:utf-8-*-

from werkzeug.exceptions import BadRequest
from src.api.errors.codes import STR_NOT_SHOULD_HAS_INT_VALUE


class StrNotShouldHasIntValues(BadRequest):

    def __init__(self, *args, **kwargs):
        self.data = {
            'detail': f"O campo '{args[0]}' não deve possuir valores numéricos.",
            'code': STR_NOT_SHOULD_HAS_INT_VALUE,
        }
        super().__init__(*args, **kwargs)
