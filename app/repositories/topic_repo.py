from sqlalchemy.orm import Session

from app.models.topic import Topic
from app.schemas.topic import TopicCreate


def createTopic(db:Session, topic: TopicCreate):
    db_topic = Topic(name=topic.name)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

def getTopics(db:Session):
    return db.query(Topic).all()


def getTopicWithDetails(db: Session, topic_id: int):
    # Buscamos el Topic por su ID y cargamos los detalles relacionados (relación uno a muchos)
    topic = db.query(Topic).filter(Topic.id == topic_id).first()

    if topic:
        # Los detalles asociados al topic se encuentran en `topic.topicsDetail`
        return topic
    return None