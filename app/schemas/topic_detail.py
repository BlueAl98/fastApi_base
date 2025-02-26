from pydantic import BaseModel
from typing import List, Optional


class TopicDetailBase(BaseModel):
    name:str

class TopicDetailCreate(TopicDetailBase):
     topicId: int

class TopicDetailResponse(TopicDetailBase):
    id: int
    topicId: int
    class Config:
        from_attributes = True
