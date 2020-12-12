#!-*-coding:utf-8-*-

from typing import List
from src.api.apps.noticias.adapters.db.models import (
    Autor as AutorModel, Noticias as NoticiaModel
)
from src.api.apps.noticias.domain.entities.noticia import Noticia
from src.api.apps.noticias.domain.inoticias_repository import (
    INoticiasRepository
)
from mongoengine.queryset.visitor import Q


class NoticiasRepository(INoticiasRepository):

    def create(self, noticia: Noticia) -> dict:
        autor_doc = AutorModel(nome=noticia.autor.nome)
        autor_doc.save()
        noticia_doc = NoticiaModel(
            titulo=noticia.titulo, texto=noticia.texto, autor=autor_doc
        )
        noticia_doc.save()
        return noticia_doc.to_dict()

    def update(self, noticia: Noticia) -> dict:
        noticia_doc = NoticiaModel.objects(id=noticia.oid).first()

        for k, v in noticia.dict().items():  # TODO: testar esse case.
            # verificando se existe o valor nome pro autor
            if isinstance(v, dict) and v['nome'] is not None:
                noticia_doc.autor.nome = v['nome']
                continue

            if v is not None:
                setattr(noticia_doc, k, v)

        noticia_doc.save()
        return noticia_doc.to_dict()

    def delete(self, noticia_id: str):
        NoticiaModel.objects(id=noticia_id).delete()

    def search_by(self, value: str) -> List[dict]:
        autor_doc = AutorModel.objects(nome__in=[value])
        noticias_doc = NoticiaModel.objects.filter(
            Q(titulo__in=[value]) | Q(texto__in=[value]) | Q(autor__in=autor_doc)
        )
        return [doc.to_dict() for doc in noticias_doc]
