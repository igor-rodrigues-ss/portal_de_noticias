#!-*-coding:utf-8-*-

from mongoengine import StringField, ReferenceField, Document


class AutorModel(Document):
    nome = StringField(max_length=512)
    meta = {'collection': 'autor'}


class NoticiaModel(Document):
    titulo = StringField(max_length=512, required=True)
    texto = StringField(required=True)
    autor = ReferenceField(AutorModel, required=True)
    meta = {'collection': 'noticia'}

    def to_dict(self) -> dict:
        return {
            'id': str(self.id),
            'titulo': self.titulo,
            'texto': self.texto,
            'autor': {
                'oid': str(self.autor.id),
                'nome': self.autor.nome
            }
        }
