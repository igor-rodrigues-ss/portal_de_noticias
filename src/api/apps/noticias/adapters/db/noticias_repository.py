#!-*-coding:utf-8-*-

from src.api.apps.noticias.adapters.db.models import (
    Autor as AutorModel, Noticias as NoticiaModel
)
from src.api.apps.noticias.domain.noticia import Noticia
from src.api.apps.noticias.domain.inoticias_repository import (
    INoticiasRepository
)
from typing import List
import json


class NoticiasRepository(INoticiasRepository):

    def _build_result(
        self, autor_model: AutorModel, noticia_model: NoticiaModel
    ) -> dict:
        noticia = json.loads(noticia_model.to_json())
        noti_oid = noticia.pop('_id')
        noticia['oid'] = noti_oid['$oid']

        autor = json.loads(autor_model.to_json())
        aut_oid = autor.pop('_id')
        autor['oid'] = aut_oid['$oid']
        noticia['autor'] = autor
        return noticia

    def create(self, noticia: Noticia):
        autor_model = AutorModel(nome=noticia.autor.nome)
        autor_model.save()
        noticia_model = NoticiaModel(
            titulo=noticia.titulo, texto=noticia.texto, autor=autor_model
        )
        noticia_model.save()
        return self._build_result(autor_model, noticia_model)

    def update(self, noticia: Noticia):
        pass

    def delete(self, noticia: Noticia):
        pass

    def search_by(self, noticia: Noticia) -> List[dict]:
        result = []
        for noticia in NoticiaModel.objects:
            result.append({
                'titulo': noticia.titulo,
                'texto': noticia.texto,
                'autor': {
                    'nome': noticia.autor.nome
                }
            })
        return result
