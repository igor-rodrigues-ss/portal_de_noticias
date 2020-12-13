#!-*-coding:utf-8-*-

import pytest
from src.api.apps.noticias.domain.operations.valid.validation_to_update import (
    ValidationToUpdate
)
from src.api.errors.exceptions import (
    StrNotShouldHasIntValues, FieldIsRequired
)


class TestValidationToUpdate:

    def test_validate_fail_autor_nome(self):
        data = {
            'id': '123456',
            'titulo': 'ABC',
            'texto': 'Teste teste teste',
            'autor': {
                'nome': 'Teste 123'
            }

        }
        with pytest.raises(StrNotShouldHasIntValues):
            ValidationToUpdate(data).validate()

    def test_validate_fail_without_id(self):
        data = {
            'id': '',
            'titulo': 'ABC',
            'texto': 'Teste teste teste',
            'autor': {
                'nome': 'Teste 123'
            }

        }
        with pytest.raises(FieldIsRequired):
            ValidationToUpdate(data).validate()

    def test_validate_success(self):
        data = {
            'id': '123456',
            'titulo': 'ABC',
            'texto': 'Teste teste teste',
            'autor': {
                'nome': 'Teste'
            }

        }
        try:
            ValidationToUpdate(data).validate()
        except Exception as exc:
            raise pytest.fail(
                f"Validação falhou com dados corretos.\n{str(exc)}"
            )
