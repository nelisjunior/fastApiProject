from typing import Annotated
from pydantic import Field

from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description="Cetro de Treinamento", example="CT Principal", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do Centro de Treinamento", example="Rua Principal, 123", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do Centro de Treinamento", example="João da Silva", max_length=30)]

