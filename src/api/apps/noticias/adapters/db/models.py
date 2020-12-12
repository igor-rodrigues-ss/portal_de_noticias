#!-*-coding:utf-8-*-

from mongoengine import StringField, ReferenceField, CASCADE, Document


class Autor(Document):
    nome = StringField(max_length=512)


class Noticias(Document):
    titulo = StringField(max_length=512, required=True)
    texto = StringField(required=True)
    autor = ReferenceField(
        Autor, reverse_delete_rule=CASCADE, required=True
        # TODO: validar a exclusão em cascata
    )

    def to_dict(self) -> dict:
        return {
            'oid': str(self.id),
            'titulo': self.titulo,
            'texto': self.texto,
            'autor': {
                'oid': str(self.autor.id),
                'nome': self.autor.nome
            }
        }
