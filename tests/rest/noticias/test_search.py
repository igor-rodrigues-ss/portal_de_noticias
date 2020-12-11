#!-*-coding:utf-8-*-

from app import app
from flask import url_for
from src.api.apps.noticias.adapters.db.models import (
    Noticias as NoticiasModel, Autor as AutorModel
)


class TestSearch:

    def setup_class(cls):
        cls.client = app.test_client()
        cls.default_headers = {'Content-Type': 'application/json'}
        cls.data = {
            'titulo': 'teste 1',
            'texto': 'teste search',
            'autor': {
                'nome': 'autor search'
            }
        }
        autor = AutorModel(nome=cls.data['autor']['nome'])
        autor.save()
        noticia = NoticiasModel(
            titulo=cls.data['titulo'], texto=cls.data['texto'], autor=autor
        )
        noticia.save()
        cls.data['oid'] = str(noticia.id)

    def test_get(self):
        val_to_test = 'teste search'
        with app.test_request_context():
            url = url_for('noticias_get_post')
            resp = self.client.get(
                f'{url}?val={val_to_test}', headers=self.default_headers
            )
        assert resp.status_code == 200
        resp_data = resp.get_json()
        assert resp_data[0]['titulo'] == self.data['titulo']
        assert resp_data[0]['texto'] == self.data['texto']
        assert resp_data[0]['autor']['nome'] == self.data['autor']['nome']

    def teardown_class(cls):
        noticia = NoticiasModel.objects.get(id=cls.data['oid'])
        noticia.delete()
