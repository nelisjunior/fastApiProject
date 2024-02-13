from sqlalchemy import DateTime, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel
from datetime import datetime


class CentroTreinamentoModel(BaseModel):
    __tablename__ = "centros_treinamento"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nm_centro: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    nm_endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    nm_proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    nm_atleta: Mapped['AtletaModel'] = relationship(back_populates='nm_centro_treinamento')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
