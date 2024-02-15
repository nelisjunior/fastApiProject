from typing import Annotated
from pydantic import Field

from workout_api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", example="Scale", max_length=10)]


class CategoriaOut(CategoriaIn):
    id: Anotated[UUID4, Field(description='Identificador da categoria')]
    created_at: Anotated[datetime, Field(description='Data de criação')]
    updated_at: Anotated[datetime, Field(description='Data de atualização')]
    deleted_at: Anotated[datetime, Field(description='Data de exclusão')]
    is_active: Anotated[bool, Field(description='Categoria ativa')]
    is_deleted: Anotated[bool, Field(description='Categoria excluída')]
