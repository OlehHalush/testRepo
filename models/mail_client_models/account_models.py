from models.base_model import ConfiguredBaseModel


class AccountRequest(ConfiguredBaseModel):
    address: str
    password: str
