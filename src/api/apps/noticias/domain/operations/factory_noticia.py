#!-*-coding:utf-8-*-

from src.api.apps.noticias.domain.entities.autor import Autor
from src.api.apps.noticias.domain.entities.noticia import Noticia

class FactoryNoticia:

    _data: dict

    def __init__(self, data: dict):
        self._data = data

    def with_optional_fields(self) -> Noticia:
        """
        - um noticia com campos opcionais e usado para atualizacao de
          uma noticia em banco
        """
        autor_json = self._data.get('autor', None)

        if isinstance(autor_json, dict):
            autor_nome = autor_json.get('nome', None)
        else:
            autor_nome = None

        autor = Autor(nome=autor_nome)
        noticia = Noticia(
            oid=self._data['oid'],
            titulo=self._data.get('titulo', None),
            texto=self._data.get('texto', None),
            autor=autor
        )
        return noticia

    def with_required_fields(self) -> Noticia:
        """
        - um noticia com campos opcionais e usado para criacao de
          uma noticia em banco
        """
        autor = Autor(nome=self._data['autor']['nome'])
        noticia = Noticia(
            titulo=self._data['titulo'], texto=self._data['texto'], autor=autor
        )
        return noticia
