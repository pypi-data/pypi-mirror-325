from pydantic import Field

from aiotrenergy.enums import RestMethod, ConsumptionType
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import PATH_LOCATION, BODY_LOCATION
from aiotrenergy.responses.consumers.update import ConsumersUpdateResponse


class ConsumersUpdateRequest(TrenergyRequest):
    __api_path__ = "consumers/{consumer_id}"
    __response__ = ConsumersUpdateResponse
    __rest_method__ = RestMethod.PATCH

    consumer_id: int = Field(json_schema_extra=PATH_LOCATION)
    name: str | None = Field(None, json_schema_extra=BODY_LOCATION)
    payment_period: int | None = Field(None, json_schema_extra=BODY_LOCATION)
    auto_renewal: bool | None = Field(None, json_schema_extra=BODY_LOCATION)
    consumption_type: ConsumptionType | None = Field(None, json_schema_extra=BODY_LOCATION)
    resource_amount: int | None = Field(None, json_schema_extra=BODY_LOCATION)

