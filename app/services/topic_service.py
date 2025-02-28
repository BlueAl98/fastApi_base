from sqlalchemy.orm import Session
from app.repositories.topic_repo import createTopic, getTopics, getTopicWithDetails
from app.schemas.topic import TopicCreate

def add_topic(db: Session, topic: TopicCreate):
    return createTopic(db, topic)

def list_topics(db: Session):
    return getTopics(db)

def getITopicRelation(db: Session, topic_id: int):
    filterobj = getTopicWithDetails(db, topic_id)
    myobj = {
        "topic": filterobj.name,
        "lista":filterobj.topicsDetail

    }

    return myobj