from typing import Annotated
from pydantic import Field

from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Cetro de Treinamento (CT)', example='CT Principal', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do CT', example='Grand Line, 123', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do CT', example='Monkey D. Luffy', max_length=30)]
