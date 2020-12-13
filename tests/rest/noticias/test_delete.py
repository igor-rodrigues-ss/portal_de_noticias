#!-*-coding:utf-8-*-

from src.app import app
from flask import url_for
from src.api.apps.noticias.adapters.db.models import NoticiaModel, AutorModel

from src.api.errors.codes import INVALID_NOTICIA_ID


class TestDelete:

    def setup_class(cls):
        cls.client = app.test_client()
        cls.default_headers = {'Content-Type': 'application/json'}

        autor = AutorModel(nome='teste')
        autor.save()
        noticia = NoticiaModel(
            titulo='teste 1', texto='teste teste 1', autor=autor
        )
        noticia.save()
        cls.noticia_id = str(noticia.id)

    def test_delete(self):
        with app.test_request_context():
            url = url_for('noticias_put_delete', noticia_id=self.noticia_id)
            resp = self.client.delete(
                url, headers=self.default_headers
            )
        assert resp.status_code == 200
        assert len(
            NoticiaModel.objects(id=self.noticia_id)
        ) == 0

    def test_delete_invalid_id(self):
        with app.test_request_context():
            url = url_for('noticias_put_delete', noticia_id='abc')
            resp = self.client.delete(
                url, headers=self.default_headers
            )
        assert resp.status_code == 400
        resp_data = resp.get_json()
        assert resp_data['code'] == INVALID_NOTICIA_ID
