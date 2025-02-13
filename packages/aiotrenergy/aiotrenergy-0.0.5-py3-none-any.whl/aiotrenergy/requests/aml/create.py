from pydantic import model_validator, Field
from typing_extensions import Self

from aiotrenergy.enums import Blockchain, RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import BODY_LOCATION
from aiotrenergy.responses.aml.create import AmlCreateResponse


class AmlCreateRequest(TrenergyRequest):
    __api_path__ = "aml/check"
    __response__ = AmlCreateResponse
    __rest_method__ = RestMethod.POST

    blockchain: Blockchain = Field(json_schema_extra=BODY_LOCATION)
    address: str | None = Field(None, json_schema_extra=BODY_LOCATION)
    txid: str | None = Field(None, json_schema_extra=BODY_LOCATION)

    @model_validator(mode="after")
    def check_api_rules_followed(self) -> Self:
        if self.blockchain == Blockchain.BTC:
            if not self.address:
                raise ValueError("address is required for BTC")
        if not self.address and not self.txid:
            raise ValueError("txid is required if address is not provided")
        return self
