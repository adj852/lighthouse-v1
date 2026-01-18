from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import date


class MetaData(BaseModel):
    id: str
    title: str
    category: str
    type: str = Field(
        description="overview | tutorial | reference | troubleshooting | flow"
    )

    tags: List[str] = Field(default_factory=list)
    arch_specific: bool = True
    last_updated: Optional[date] = None


class KnowledgeEntry(BaseModel):
    meta: MetaData
    data: Dict[str, Any]

