from uuid import UUID
from pydantic import BaseModel, ConfigDict

from app.models.asset import AssetKind

class AssetOut(BaseModel):
    id: UUID
    kind: AssetKind
    url: str
    mime_type: str
    size_bytes: int

    model_config = ConfigDict(from_attributes=True)