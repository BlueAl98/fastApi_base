from sqlalchemy.orm import Session

from app.models.topicDetail import TopicDetail
from app.schemas.topic_detail import TopicDetailCreate

def CreateTopicDetail(db:Session, topic: TopicDetailCreate):
    db_topic = TopicDetail(name=topic.name, topicId=topic.topicId)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

def getTopicsDetail(db:Session):
    return db.query(TopicDetail).all()