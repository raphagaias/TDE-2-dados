from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR
from sqlalchemy import INTEGER, ForeignKey, DATE
from datetime import date
from models.usuario import usuario

class Playlists(Base):
    __tablename__ = "Playlist"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True, autoincrement=True, nullable= False)
    playlist_name: Mapped[str] = mapped_column("videos", VARCHAR(255), nullable=False)
    created_at: Mapped[date] = mapped_column("created_at",DATE, nullable=True)
    usuario_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(usuario.id), unique=True, nullable=False)
    