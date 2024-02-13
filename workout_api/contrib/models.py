from sqlalchemy import Column, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from uuid import uuid4
from datetime import datetime

from sqlalchemy import Column, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime

DeclarativeBase = declarative_base()


class BaseModel(DeclarativeBase):
    __abstract__ = True
    id: Mapped[UUID] = Column(UUID(as_uuid=True), default=uuid4, nullable=False)
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at: Mapped[datetime] = Column(DateTime, nullable=True)
    is_active: Mapped[bool] = Column(Boolean, default=True)
    is_deleted: Mapped[bool] = Column(Boolean, default=False)
