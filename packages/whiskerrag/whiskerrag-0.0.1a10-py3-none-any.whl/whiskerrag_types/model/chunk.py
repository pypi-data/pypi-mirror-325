from dataclasses import Field
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_serializer, Field

from .knowledge import EmbeddingModelEnum


class Chunk(BaseModel):
    chunk_id: str = Field(None, description="chunk id")
    embedding: Optional[list[float]] = Field(None, description="chunk embedding")
    context: str = Field(..., description="chunk content")
    knowledge_id: str = Field(None, description="file source info")
    embedding_model_name: Optional[EmbeddingModelEnum] = Field(
        EmbeddingModelEnum.OPENAI, description="name of the embedding model"
    )
    space_id: str = Field(..., description="space id")
    metadata: Optional[dict] = Field(None, description="metadata")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().isoformat(), description="creation time"
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now().isoformat(), description="update time"
    )

    @field_serializer("created_at")
    def serialize_created_at(self, created_at: Optional[datetime]):
        return created_at.isoformat() if created_at else None

    @field_serializer("updated_at")
    def serialize_updated_at(self, updated_at: Optional[datetime]):
        return updated_at.isoformat() if updated_at else None

    @field_serializer("embedding_model_name")
    def serialize_embedding_model_name(self, embedding_model_name):
        if isinstance(embedding_model_name, EmbeddingModelEnum):
            return embedding_model_name.value
        return str(embedding_model_name)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.updated_at = datetime.now().isoformat()
        return self
