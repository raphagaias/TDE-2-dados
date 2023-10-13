from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR
from sqlalchemy import INTEGER, ForeignKey, BOOLEAN, DECIMAL

class Categories(Base):
    __tablename__ = "Category"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True, autoincrement=True, nullable= False, unique=True)
    name: Mapped[str] = mapped_column("nome", VARCHAR(45), nullable=False, unique = True)
