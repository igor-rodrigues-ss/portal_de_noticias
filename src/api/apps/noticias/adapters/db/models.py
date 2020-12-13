#!-*-coding:utf-8-*-

from mongoengine import StringField, ReferenceField, CASCADE, Document


class AutorModel(Document):
    nome = StringField(max_length=512)
    meta = {
        'collection': 'autor',
        'indexes': [{
            'fields': ['$nome'],
            'weights': {'nome': 3}
        }]
    }


class NoticiaModel(Document):
    titulo = StringField(max_length=512, required=True)
    texto = StringField(required=True)
    autor = ReferenceField(
        AutorModel, reverse_delete_rule=CASCADE, required=True
    )
    meta = {
        'collection': 'noticia',
        'indexes': [{
            'fields': ['$titulo', '$texto'],
            # 'default_language': 'english',
            'weights': {'titulo': 10, 'texto': 2}
        }]
    }

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
