#!-*-coding:utf-8-*-

from werkzeug.exceptions import BadRequest
from src.api.errors.codes import STR_NOT_SHOULD_HAS_INT_VALUE
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
