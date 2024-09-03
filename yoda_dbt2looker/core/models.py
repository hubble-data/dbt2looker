from typing import Dict, List, Optional, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from pydantic import Field, validator, BaseModel

from yoda_dbt2looker.models import (
    DbtNode,
    DbtModelColumn,
    ModelIntegrationConfigMetadata,
    DbtManifestMetadata
)


class DbtModelMeta(BaseModel):
    primary_key: Optional[str] = Field(None, alias="primary-key")
    integration_config: Optional[ModelIntegrationConfigMetadata] = None


class DbtModelConfig(BaseModel):
    tags: Optional[List[str]] = None


class DbtModel(DbtNode):
    resource_type: Literal["model"]
    relation_name: str
    db_schema: str = Field(..., alias="schema")
    name: str
    description: str
    columns: Dict[str, DbtModelColumn]
    tags: List[str]
    meta: DbtModelMeta
    config: DbtModelConfig

    @validator("columns")
    def case_insensitive_column_names(cls, v: Dict[str, DbtModelColumn]):
        return {
            name.lower(): column.copy(update={"name": column.name.lower()})
            for name, column in v.items()
        }


class DbtManifest(BaseModel):
    nodes: Dict[str, Union[DbtModel, DbtNode]]
    metadata: DbtManifestMetadata
