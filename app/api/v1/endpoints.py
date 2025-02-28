from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db.session import get_db
from app.schemas.topic import TopicResponse, TopicCreate
from app.schemas.topic_detail import TopicDetailResponse, TopicDetailCreate
from app.services.user_service import add_user, list_users
from app.schemas.user import UserCreate, UserOut
from app.services.topic_service import list_topics, add_topic, getITopicRelation
from app.services.topic_details_service import add_topicDetail, list_topicsDetail
from typing import List

router = APIRouter()


@router.post("/users/", response_model=UserOut)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return add_user(db, user)


@router.get("/users/", response_model=List[UserOut])
def get_users_endpoint(db: Session = Depends(get_db)):
    return list_users(db)


@router.post("/topic/", response_model=TopicResponse)
def createTopic_endpoint(topic: TopicCreate, db: Session = Depends(get_db)):
    return add_topic(db, topic)


@router.get("/topic/", response_model=List[TopicResponse])
def getTopics_endpoint(db: Session = Depends(get_db)):
    return list_topics(db)


@router.post("/topic_detail/", response_model=TopicDetailResponse)
def createTopicDetail(topic: TopicDetailCreate, db: Session = Depends(get_db)):
    return add_topicDetail(db, topic)


@router.get("/topic/{topic_id}")
def get_topic_with_details(topic_id: int, db: Session = Depends(get_db)):
    return getITopicRelation(db, topic_id)


