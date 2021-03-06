#!-*-coding:utf-8-*-

from src.app import app
from flask import url_for
from src.api.apps.noticias.adapters.db.models import NoticiaModel, AutorModel


class TestSearch:

    @classmethod
    def _save_data(cls, data: dict):
        autor = AutorModel(nome=data['autor']['nome'])
        autor.save()
        noticia = NoticiaModel(
            titulo=data['titulo'], texto=data['texto'], autor=autor
        )
        noticia.save()
        return str(noticia.id)

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
        cls.data2 = {
            'titulo': 'abc',
            'texto': 'abc',
            'autor': {
                'nome': 'abc'
            }
        }
        cls.data['oid'] = cls._save_data(cls.data)
        cls.data2['oid'] = cls._save_data(cls.data2)

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
        noticias = NoticiaModel.objects.filter(
            id__in=[cls.data2['oid'], cls.data['oid']]
        )
        noticias.delete()
