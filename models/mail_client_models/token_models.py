from models.base_model import ConfiguredBaseModel
from pydantic import Field


class TokenRequest(ConfiguredBaseModel):
    address: str
    password: str


class TokenResponse(ConfiguredBaseModel):
    at_id: str = Field(alias='@id')
    id: str
    token: str
