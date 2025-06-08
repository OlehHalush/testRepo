from typing import List, Optional

from pydantic import Field

from models.base_model import ConfiguredBaseModel


class EmailAddress(ConfiguredBaseModel):
    address: str
    name: Optional[str] = ""


class TLSVerification(ConfiguredBaseModel):
    name: str
    standardName: str
    version: str


class Verifications(ConfiguredBaseModel):
    dkim: bool
    spf: bool
    tls: TLSVerification


class MessageDetailsResponse(ConfiguredBaseModel):
    context: str = Field(..., alias="@context")
    id_: str = Field(..., alias="@id")
    type_: str = Field(..., alias="@type")
    accountId: str
    bcc: List[EmailAddress]
    cc: List[EmailAddress]
    createdAt: str
    downloadUrl: str
    flagged: bool
    from_: EmailAddress = Field(..., alias="from")
    hasAttachments: bool
    html: List[str]
    id: str
    intro: str
    isDeleted: bool
    msgid: str
    retention: bool
    retentionDate: str
    seen: bool
    size: int
    sourceUrl: str
    subject: str
    text: str
    to: List[EmailAddress]
    updatedAt: str
    verifications: Verifications
