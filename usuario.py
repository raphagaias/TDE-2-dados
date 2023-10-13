from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import INTEGER, VARCHAR
from sqlalchemy.dialects.mysql import BOOLEAN, DATE
from datetime import date


class usuario(Base):
    __tablename__ = "usuario"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True, autoincrement=True, nullable= False, unique=True)
    birthday: Mapped[date] = mapped_column("birthday",DATE, nullable=False)
    name: Mapped[str] = mapped_column("usuarioname",VARCHAR(255), nullable= False, unique = True)
    email: Mapped[str] = mapped_column("email",VARCHAR(45), nullable=False, unique = True)
    created_at:Mapped[date] = mapped_column("created_at", DATE, nullable=True)
    registred: Mapped[bool] = mapped_column("registred",BOOLEAN, nullable=False)
