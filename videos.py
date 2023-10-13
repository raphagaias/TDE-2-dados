from models import Base, Categories
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import VARCHAR
from sqlalchemy import INTEGER, ForeignKey, BOOLEAN, TEXT, DATE
from datetime import date
from models.usuario import usuario

class Videos(Base):
    __tablename__ = "videos"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True, autoincrement=True, nullable= False, unique=True)
    title: Mapped[str] = mapped_column("title", VARCHAR(255), nullable=False)
    description: Mapped[str] = mapped_column("description", TEXT)
    usuario_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(usuario.id), nullable=False)
    category_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Categories.id), nullable=False)
    created_at: Mapped[date] = mapped_column("created_at", DATE)
    sensivel: Mapped[bool] = mapped_column("sensivel",BOOLEAN, nullable=False)
