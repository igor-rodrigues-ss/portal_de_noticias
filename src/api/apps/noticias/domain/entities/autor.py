from pydantic import BaseModel


class Autor(BaseModel):
    nome: str
    oid: str = None
