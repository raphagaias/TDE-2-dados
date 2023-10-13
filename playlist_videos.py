from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, DATE
from models.playlists import Playlists
from models.videos import Videos
from datetime import date

class Playlist_videos(Base):
    __tablename__ = "playlist_videos"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True, autoincrement=True, nullable= False)
    playlist_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Playlists.id),nullable=False)
    video_id: Mapped[int] = mapped_column(INTEGER, ForeignKey(Videos.id),nullable=False)
    created_at: Mapped[date] = mapped_column("created_at", DATE, nullable=False)