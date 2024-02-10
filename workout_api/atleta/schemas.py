from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema


class Atleta(BaseModel):
    nome: Annotated[str, Field(description="Nome do atleta", example="João da Silva", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678900", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=75.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=1.75)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M ou F", max_length=1)]
    centro_treinamento_id: Annotated[int, Field(description="ID do centro de treinamento do atleta", example=1)]
    categoria_id: Annotated[int, Field(description="ID da categoria do atleta", example=1)]
