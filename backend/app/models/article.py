import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy import ForeignKey, String, Uuid

from app.core.db import Base
from app.core.types import JSONVariant

# default tiptap doc: empty
def empty_doc():
    return { "type": "doc", "content": [{ "type": "paragraph" }]}

class Article(Base):
    __tablename__ = "articles"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(500), nullable=False, default="Untitled")
    content: Mapped[str] = mapped_column(JSONVariant, nullable=False, default= lambda: empty_doc)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now(), nullable=False)