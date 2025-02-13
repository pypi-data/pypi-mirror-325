from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import BODY_LOCATION
from aiotrenergy.responses.consumers.toggle_auto_renewal import ConsumersToggleAutoRenewalResponse


class ConsumersToggleAutoRenewalRequest(TrenergyRequest):
    __api_path__ = "consumers/auto-renewal"
    __response__ = ConsumersToggleAutoRenewalResponse
    __rest_method__ = RestMethod.POST

    auto_renewal: bool = Field(json_schema_extra=BODY_LOCATION)
    consumers: list[int] = Field(json_schema_extra=BODY_LOCATION)
