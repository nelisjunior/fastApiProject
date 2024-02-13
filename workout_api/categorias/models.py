from sqlalchemy import DateTime, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel
from datetime import datetime


class CategoriaModel(BaseModel):
    __tablename__ = "categorias"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nm_categoria: Mapped[str] = mapped_column(String(50), nullable=False)
    atletas: Mapped['AtletaModel'] = relationship('AtletaModel', back_populates='categoria')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)