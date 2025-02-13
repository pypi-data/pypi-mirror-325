from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import BODY_LOCATION
from aiotrenergy.responses.consumers.activate_address import ConsumersActivateAddressResponse


class ConsumersActivateAddressRequest(TrenergyRequest):
    __api_path__ = "extra/activate-address"
    __response__ = ConsumersActivateAddressResponse
    __rest_method__ = RestMethod.POST

    address: str = Field(json_schema_extra=BODY_LOCATION)