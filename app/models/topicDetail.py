from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db.session import Base

class TopicDetail(Base):
    __tablename__ = "topics_detail"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    topicId = Column(Integer, ForeignKey("topics.id"))

    topic = relationship("Topic", back_populates="topicsDetail")





