#!-*-coding:utf-8-*-


import json
from app import app
from flask import url_for
from src.api.apps.noticias.adapters.db.models import (
    Noticias as NoticiasModel, Autor as AutorModel
)


class TestUpdate:

    def setup_class(cls):
        cls.client = app.test_client()
        cls.default_headers = {'Content-Type': 'application/json'}
        autor = AutorModel(nome='teste')
        autor.save()
        noticia = NoticiasModel(
            titulo='teste 1', texto='teste teste 1', autor=autor
        )
        noticia.save()
        cls.new_data = {
            'titulo': 'teste',
            'texto': 'teste update',
            'autor': {
                'nome': 'autor update'
            }
        }
        cls.created_data = []
        cls.noticia_id = str(noticia.id)

    def test_update(self):
        with app.test_request_context():
            url = url_for('noticias_put_delete', noticia_id=self.noticia_id)
            resp = self.client.put(
                url, data=json.dumps(self.new_data),
                headers=self.default_headers
            )
        assert resp.status_code == 200
        resp_data = resp.get_json()
        self.created_data.append(resp_data)
        assert resp_data['titulo'] == self.new_data['titulo']
        assert resp_data['texto'] == self.new_data['texto']
        assert resp_data['autor']['nome'] == self.new_data['autor']['nome']

    def teardown_class(cls):
        for data in cls.created_data:
            noticia = NoticiasModel.objects.get(id=data['oid'])
            noticia.delete()
