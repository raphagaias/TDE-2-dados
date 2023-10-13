from models import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from models.videos import Videos

class video_tag(Base):
    __tablename__ = "video_tag"
    id: Mapped[int] = mapped_column("id",INTEGER, primary_key=True, autoincrement=True, nullable= False)
    tag_name: Mapped[str] = mapped_column("name", VARCHAR(255), nullable=False)
    video_id: Mapped[int]= mapped_column(INTEGER, ForeignKey(Videos.id), nullable=False)
