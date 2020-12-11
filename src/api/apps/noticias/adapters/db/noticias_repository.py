#!-*-coding:utf-8-*-

from typing import List
from src.api.apps.noticias.adapters.db.models import (
    Autor as AutorModel, Noticias as NoticiaModel
)
from src.api.apps.noticias.domain.noticia import Noticia
from src.api.apps.noticias.domain.inoticias_repository import (
    INoticiasRepository
)
from mongoengine.queryset.visitor import Q


class NoticiasRepository(INoticiasRepository):

    def create(self, noticia: Noticia) -> dict:
        autor_model = AutorModel(nome=noticia.autor.nome)
        autor_model.save()
        noticia_model = NoticiaModel(
            titulo=noticia.titulo, texto=noticia.texto, autor=autor_model
        )
        noticia_model.save()
        return noticia_model.to_dict()

    def update(self, noticia: Noticia) -> dict:
        noticia_doc = NoticiaModel.objects(id=noticia.oid).first()

        for k, v in noticia.dict().items():  # TODO: testar esse case.
            if isinstance(v, dict) and v['nome'] is not None:
                noticia_doc.autor.nome = v['nome']
                continue

            if v is not None:
                setattr(noticia_doc, k, v)

        noticia_doc.save()
        return noticia_doc.to_dict()

    def delete(self, noticia_id: str):
        NoticiaModel.objects(id=noticia_id).delete()

    def search_by(self, value: str) -> List:
        autor = AutorModel.objects(nome__in=[value])
        noticias = NoticiaModel.objects.filter(
            Q(titulo__in=[value]) | Q(texto__in=[value]) | Q(autor__in=autor)
        )
        return [doc.to_dict() for doc in noticias]
