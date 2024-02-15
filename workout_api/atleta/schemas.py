from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema
from workout_api.atleta.schemas import AtletaIn


class AtletaIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example="João da Silva", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678900", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=75.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=1.75)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M ou F", max_length=1)]


class AtletaOut(AtletaIn):
    id: Annotated[UUID4, Field(description='Identificador único')]
    created_at: Annotated[datetime, Field(description='Data de criação')]
    updated_at: Annotated[datetime, Field(description='Data de atualização')]
    deleted_at: Annotated[datetime, Field(description='Data de exclusão', nullable=True)]
    is_active: Annotated[bool, Field(description='Ativo')]
    is_deleted: Annotated[bool, Field(description='Deletado')]
    id_centro_treinamento: Annotated[int, Field(description='Identificador do centro de treinamento')]
    id_categoria: Annotated[int, Field(description='Identificador da categoria')]