from fastapi import APIRouter, Body, status
from workout_api.contrib.dependencies import DatabaseDependency

from workout_api.categorias.schemas import CategoriaIn, CategoriaOut

router = APIRouter()


@router.post(
    '/',
    summary='Cria nova categoria',
    status_code=status.HTTP_201_CREATED,
    reponse_model=CategoriaOut,
)
async def post(
        db_session: DatabaseDependency,
        categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in)
    pass
