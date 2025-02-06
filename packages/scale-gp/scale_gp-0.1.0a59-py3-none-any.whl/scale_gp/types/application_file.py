# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ApplicationFile"]


class ApplicationFile(BaseModel):
    id: str

    account_id: str
    """The ID of the account that owns the given entity."""

    created_at: datetime
    """The date and time when the entity was created in ISO format."""

    created_by_user_id: str
    """The user who originally created the entity."""

    file_name: str

    file_size_bytes: int

    file_artifact_blob_path: Optional[str] = None
