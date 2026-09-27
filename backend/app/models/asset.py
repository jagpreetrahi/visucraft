import enum
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from datetime import datetime
from sqlalchemy import BigInteger, Enum, ForeignKey, String, Uuid # Uuid for the db independet UUID type handling
from sqlalchemy.sql import func

from app.core.db import Base
from app.core.types import JSONVariant

class AssetKind(str, enum.Enum):
    CODE_SNAPSHOT = "code_snapshot"
    CANVAS_SNAPSHOT = "canvas_snapshot"
    IMAGE = "image"

class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    kind: Mapped[AssetKind] = mapped_column(Enum(AssetKind, native_enum=False), nullable=False)

    storage_key: Mapped[str] = mapped_column(String(500), nullable=False)
    original_url: Mapped[str | None] = mapped_column(String(200), nullable=True)
    mime_type: Mapped[str] = mapped_column(String(100), nullable=False)
    size_bytes: Mapped[int] = mapped_column(BigInteger, nullable=False)
    meta: Mapped[dict] = mapped_column(JSONVariant, nullable=False, default=dict)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
