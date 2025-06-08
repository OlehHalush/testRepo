from datetime import datetime
from typing import List

from pydantic import Field

from models.base_model import ConfiguredBaseModel


class Domain(ConfiguredBaseModel):
    id: str
    domain: str
    isActive: bool
    isPrivate: bool
    createdAt: datetime
    updatedAt: datetime


class DomainsResponse(ConfiguredBaseModel):
    context: str = Field(alias='@context')
    id_: str = Field(alias='@id')
    type_: str = Field(alias='@type')
    hydra_member: List[Domain] = Field(alias='hydra:member')
    hydra_totalItems: int = Field(alias='hydra:totalItems')
