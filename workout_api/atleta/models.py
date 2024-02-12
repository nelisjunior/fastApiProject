from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True ,nullable=False)
    idade: Mapped[str] = mapped_column(Integer, nullable=False)
    peso: Mapped[Float] = mapped_column(Float, nullable=False)
    altura: Mapped[Float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atletas')
    centro_treinamento_id: Mapped[int] = mapped_column(Integer, ForeignKey("centros_treinamento.pk_id"))
    
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atletas')
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"))
    
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
