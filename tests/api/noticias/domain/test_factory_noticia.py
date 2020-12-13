#!-*-coding:utf-8-*-

from src.api.apps.noticias.domain.operations.factory_noticia import (
    FactoryNoticia
)


class TestFactoryNoticia:

    def test_factory_to_create(self):
        data = {
            'titulo': 'ABC',
            'texto': 'Teste teste teste',
            'autor': {
                'nome': 'Teste'
            }

        }
        noticia = FactoryNoticia(data).to_create()
        assert noticia.titulo == data['titulo']
        assert noticia.texto == data['texto']
        assert noticia.autor.nome == data['autor']['nome']

    def test_factory_to_update(self):
        data = {
            'id': '123456789',
            'autor': {
                'nome': 'Teste'
            }

        }
        noticia = FactoryNoticia(data).to_update()
        assert noticia.titulo is None
        assert noticia.texto is None
        assert noticia.autor.nome == data['autor']['nome']


    # def test_validate_success(self):
    #     data = {
    #         'titulo': 'ABC',
    #         'texto': 'Teste teste teste',
    #         'autor': {
    #             'nome': 'Teste'
    #         }

    #     }
    #     noticia = FactoryNoticia(data).with_required_fields()
    #     try:
    #         Validation(noticia).validate()
    #     except Exception as exc:
    #         raise pytest.fail(
    #             f"Validação falhou com dados corretos.\n{str(exc)}"
    #         )
