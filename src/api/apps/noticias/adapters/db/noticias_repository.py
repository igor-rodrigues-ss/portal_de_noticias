#!-*-coding:utf-8-*-

from typing import List
from src.api.apps.noticias.adapters.db.models import AutorModel, NoticiaModel
from src.api.apps.noticias.domain.entities.noticia import Noticia
from src.api.apps.noticias.domain.inoticias_repository import (
    INoticiasRepository
)
from mongoengine.queryset.visitor import Q
from mongoengine.errors import ValidationError as ValidationErrorMongo
from mongoengine import DoesNotExist
from src.api.errors.exceptions import InvalidNoticiaID
from src.log import log


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
        update_autor = False
        try:
            noticia_doc = NoticiaModel.objects.get(id=noticia.oid)
        except ValidationErrorMongo:
            raise InvalidNoticiaID(noticia.oid)
        except DoesNotExist:
            log.info(
                'Tentativa de atualização de notícia com ID inexistente na base.'
            )
            return {}

        for k, v in noticia.dict().items():
            # verificando se o autor possui nome para update
            if k == 'autor':
                if isinstance(v, dict) and v['nome'] is not None:
                    noticia_doc.autor.nome = v['nome']
                    update_autor = True
                continue

            # setando novos valores para atualizacao
            if v is not None:
                setattr(noticia_doc, k, v)

        if update_autor:
            noticia_doc.autor.save()

        noticia_doc.save()
        return noticia_doc.to_dict()

    def delete(self, noticia_id: str):
        try:
            noticia_doc = NoticiaModel.objects.get(id=noticia_id)
        except ValidationErrorMongo:
            raise InvalidNoticiaID(noticia_id)
        except DoesNotExist:
            log.info(
                'Tentativa de remoção de notícia com ID inexistente na base.'
            )
            return

        noticia_doc.autor.delete()
        noticia_doc.delete()

    def search_by(self, value: str) -> List[dict]:
        autor_doc = AutorModel.objects.filter(nome__icontains=value)
        noticias_doc = NoticiaModel.objects.filter(
            Q(titulo__icontains=value) | Q(texto__icontains=value) | Q(autor__in=autor_doc)
        )
        return [doc.to_dict() for doc in noticias_doc]
