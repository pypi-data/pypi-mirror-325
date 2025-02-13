from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import PATH_LOCATION
from aiotrenergy.responses.consumers.deactivate import ConsumersDeactivateResponse


class ConsumersDeactivateRequest(TrenergyRequest):
    __api_path__ = "consumers/{consumer_id}/deactivate"
    __response__ = ConsumersDeactivateResponse
    __rest_method__ = RestMethod.POST

    consumer_id: int = Field(json_schema_extra=PATH_LOCATION)
