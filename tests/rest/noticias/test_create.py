#!-*-coding:utf-8-*-

import json
from app import app
from flask import url_for
from src.api.apps.noticias.adapters.db.models import Noticias as NoticiasModel


class TestCreate:

    def setup_class(cls):
        cls.client = app.test_client()
        cls.default_headers = {'Content-Type': 'application/json'}
        cls.data = {
            "titulo": "teste",
            "texto": "teste teste",
            "autor": {
                "nome": "teste"
            }
        }
        cls.created_data = []

    def test_post(self):
        with app.test_request_context():
            url = url_for('noticias_get_post')
            resp = self.client.post(
                url, data=json.dumps(self.data), headers=self.default_headers
            )
        assert resp.status_code == 200
        resp_data = resp.get_json()
        self.created_data.append(resp_data)
        assert resp_data['titulo'] == self.data['titulo']
        assert resp_data['texto'] == self.data['texto']
        assert resp_data['autor']['nome'] == self.data['autor']['nome']

    def teardown_class(cls):
        for data in cls.created_data:
            noticia = NoticiasModel.objects.get(id=data['oid'])
            noticia.delete()
