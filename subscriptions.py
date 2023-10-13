from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer
from sqlalchemy import INTEGER, ForeignKey, DATE
from datetime import date

class subscriptions(Base):
    __tablename__ = "subscriptions"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True, autoincrement=True, nullable= False)
    subscriber_id: Mapped[int] = mapped_column(INTEGER, ForeignKey("usuario.id"), nullable=False)
    usuario_id: Mapped[int] = mapped_column(INTEGER, ForeignKey("usuario.id"), nullable=False)
    created_at: Mapped[date] = mapped_column( "created_at", DATE, nullable=True)