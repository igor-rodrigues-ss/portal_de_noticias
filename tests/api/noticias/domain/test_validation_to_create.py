#!-*-coding:utf-8-*-

import pytest
from src.api.apps.noticias.domain.operations.valid.validation_to_create import (
    ValidationToCreate
)
from src.api.errors.exceptions import FieldNotShouldHasNumbers


class TestValidationToCreate:

    def test_validate_fail(self):
        data = {
            'titulo': 'ABC',
            'texto': 'Teste teste teste',
            'autor': {
                'nome': 'Teste 123'
            }

        }
        with pytest.raises(FieldNotShouldHasNumbers):
            ValidationToCreate(data).validate()

    def test_validate_success(self):
        data = {
            'titulo': 'ABC',
            'texto': 'Teste teste teste',
            'autor': {
                'nome': 'Teste'
            }

        }
        try:
            ValidationToCreate(data).validate()
        except Exception as exc:
            raise pytest.fail(
                f"Validação falhou com dados corretos.\n{str(exc)}"
            )
