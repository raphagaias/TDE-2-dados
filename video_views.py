from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, DATE
from datetime import date
from models.videos import usuario, Videos

class video_views(Base):
    __tablename__ = "video_views"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True, autoincrement=True, nullable= False)
    usuario_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(usuario.id), nullable=True)
    video_id: Mapped[int]= mapped_column(INTEGER, ForeignKey(Videos.id), nullable=False)
