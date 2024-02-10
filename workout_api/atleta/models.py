from sqlalchemy import Float
from workout_api.models.base_model import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    idade: Mapped[str] = mapped_column(Integer, nullable=False)
    peso: Mapped[Float] = mapped_column(Float, nullable=False)
    altura: Mapped[Float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    centro_treinamento_id: Mapped[int] = mapped_column(Integer, ForeignKey("centros_treinamento.pk_id"), nullable=False)
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey("categorias.pk_id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
