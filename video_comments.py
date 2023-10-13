from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR
from sqlalchemy import INTEGER, ForeignKey, DATE
from models.videos import Videos
from datetime import date
from models import usuario

class video_comments(Base):
    __tablename__ = "video_comments"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True, autoincrement=True, nullable= False, unique=True)
    comment_text: Mapped[str] = mapped_column("comment_text", VARCHAR(256), nullable=True)
    usuario_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(usuario.id), nullable=False)
    video_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Videos.id), nullable=False)
    created_at: Mapped[date] = mapped_column("created_at",DATE, nullable=True)
 