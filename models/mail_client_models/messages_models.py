from typing import List, Optional

from pydantic import Field

from models.base_model import ConfiguredBaseModel


class EmailContact(ConfiguredBaseModel):
    address: str
    name: Optional[str]


class Message(ConfiguredBaseModel):
    at_id: str = Field(alias='@id')
    at_type: str = Field(alias='@type')
    accountId: str
    createdAt: str
    downloadUrl: str
    from_: EmailContact = Field(alias='from')
    hasAttachments: bool
    id: str
    intro: str
    isDeleted: bool
    msgid: str
    seen: bool
    size: int
    sourceUrl: str
    subject: str
    to: List[EmailContact]
    updatedAt: str


class MessagesResponse(ConfiguredBaseModel):
    context: str = Field(alias='@context')
    at_id: str = Field(alias='@id')
    at_type: str = Field(alias='@type')
    hydra_member: List[Message] = Field(alias='hydra:member')
    hydra_totalItems: int = Field(alias='hydra:totalItems')
