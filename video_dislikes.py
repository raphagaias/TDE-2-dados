from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, DATE, INTEGER
from datetime import date
from models.usuario import usuario
from models.videos import Videos

class video_dislikes(Base):
    __tablename__ = "video_dislikes"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True,autoincrement=True, nullable= False)
    usuario_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(usuario.id), nullable=False)
    video_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Videos.id), nullable=False)