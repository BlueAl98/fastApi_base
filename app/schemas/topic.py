from pydantic import BaseModel
from typing import List, Optional
from app.schemas.topic_detail import TopicDetailResponse


class TopicBase(BaseModel):
    name:str

class TopicCreate(TopicBase):
    pass

class TopicResponse(TopicBase):
    id: int
    topicsDetails: List[TopicDetailResponse] = []

    class Config:
        from_attributes = True
