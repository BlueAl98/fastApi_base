from pydantic import BaseModel
from typing import List, Optional


class TopicDetailBase(BaseModel):
    name: str
    topicId: int

class TopicDetailCreate(TopicDetailBase):
    pass
    # topicId: int

class TopicDetailResponse(TopicDetailBase):
    id: int
    name: str
    #topicId: int

    class Config:
        from_attributes = True
