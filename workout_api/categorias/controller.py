from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut, CategoriaUpdate
from workout_api.categorias.models import CategoriaModel

from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()


@router.post(
    '/',
    summary='Criar uma nova Categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
        db_session: DatabaseDependency,
        categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out


@router.get(
    '/',
    summary='Consultar todas as Categorias',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(db_session: DatabaseDependency) -> list[CategoriaOut]:
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()

    return categorias

@router.get(
    '/{id}',
    summary='Consultar uma Categoria pelo id',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def get(id: UUID4, db_session: DatabaseDependency) -> CategoriaOut:
    categoria: CategoriaOut = (
        await db_session.execute(select(CategoriaModel).filter_by(id=id))
    ).scalars().first()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Categoria não encontrada no id: {id}'
        )

    return categoria


@router.patch(
    '/{id}',
    summary='Atualizar uma Categoria pelo id',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def patch(id: UUID4, db_session: DatabaseDependency, categoria_up: CategoriaUpdate = Body(...)) -> CategoriaOut:
    categoria: CategoriaOut = (
        await db_session.execute(select(CategoriaModel).filter_by(id=id))
    ).scalars().first()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Categoria não encontrada no id: {id}'
        )

    categoria_update = categoria_up.dict(exclude_unset=True)
    for key, value in categoria_update.items():
        setattr(categoria, key, value)

    await db_session.commit()
    await db_session.refresh(categoria)

    return categoria


@router.delete(
    '/{id}',
    summary='Remover uma Categoria pelo id',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(id: UUID4, db_session: DatabaseDependency):
    categoria: CategoriaOut = (
        await db_session.execute(select(CategoriaModel).filter_by(id=id))
    ).scalars().first()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Categoria não encontrada no id: {id}'
        )

    await db_session.delete(categoria)
    await db_session.commit()
