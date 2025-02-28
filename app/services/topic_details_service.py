

from sqlalchemy.orm import Session
from app.repositories.topicDetail_repo import getTopicsDetail, CreateTopicDetail
from app.schemas.topic_detail import TopicDetailCreate

def add_topicDetail(db: Session, topicDetail: TopicDetailCreate):
    return CreateTopicDetail(db, topicDetail)

def list_topicsDetail(db: Session):
    return getTopicsDetail(db)