from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

class ArticleCreate(BaseModel):
    title: str = Field(default="Untitled", max_length=500)

class ArticleUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=500)
    content: dict[str, Any] | None = None

class ArticleSummary(BaseModel):
    id: UUID
    title: str
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class ArticleOut(BaseModel):
    id: UUID
    title: str
    content: dict[str, Any]
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
