from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.topicDetail import TopicDetail
from app.core.db.session import Base

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))

    topicsDetail = relationship("TopicDetail", back_populates="topic")


