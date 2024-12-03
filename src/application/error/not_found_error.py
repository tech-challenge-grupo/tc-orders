from dataclasses import dataclass
from typing import Dict, Optional

from src.domain.__shared.error import DomainError


@dataclass(frozen=True, kw_only=True, slots=True)
class NotFoundError(DomainError):
    """Base class for errors where an entity is not found."""

    message: str = "Not found"
    search_params: Dict[str, Optional[object]]


__all__ = ["NotFoundError"]