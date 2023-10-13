from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer
from sqlalchemy import INTEGER, ForeignKey
from models import usuario
from models.videos import Videos

class video_likes(Base):
    __tablename__ = "video_likes"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True, autoincrement=True, nullable= False, unique=True)
    video_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Videos.id), nullable=False)
    usuario_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(usuario.id), nullable=False)
    
