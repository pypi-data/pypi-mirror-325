import decimal

from pydantic import field_validator, HttpUrl, Field

from aiotrenergy.enums import RestMethod, ConsumptionType
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import BODY_LOCATION
from aiotrenergy.responses.consumers.create import ConsumersCreateResponse


class ConsumersCreateRequest(TrenergyRequest):
    __api_path__ = "consumers"
    __response__ = ConsumersCreateResponse
    __rest_method__ = RestMethod.POST

    payment_period: int = Field(json_schema_extra=BODY_LOCATION)
    address: str = Field(json_schema_extra=BODY_LOCATION)
    auto_renewal: bool = Field(json_schema_extra=BODY_LOCATION)
    consumption_type: ConsumptionType = Field(json_schema_extra=BODY_LOCATION)
    resource_amount: int = Field(None, json_schema_extra=BODY_LOCATION)
    name: str | None = Field(json_schema_extra=BODY_LOCATION)
    webhook_url: HttpUrl | None = Field(None, json_schema_extra=BODY_LOCATION)

    @field_validator("resource_amount", "consumption_type")
    @classmethod
    def check_resource_amount(cls, v, values):
        if v is None and values["consumption_type"] == ConsumptionType.STATIC:
            raise ValueError("resource_amount is required for STATIC (1) consumption_type")
        return v
