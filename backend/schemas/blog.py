from typing import Optional
from pydantic import BaseModel, model_validator
from datetime import datetime


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @model_validator(mode="before")
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values["title"].replace(" ", "-").lower()
        return values


class ShowBlog(BaseModel):
    title: str
    content: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
