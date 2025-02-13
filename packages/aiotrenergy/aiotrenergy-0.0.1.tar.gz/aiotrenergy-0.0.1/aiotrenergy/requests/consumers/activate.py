from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import PATH_LOCATION
from aiotrenergy.responses.consumers.activate import ConsumersActivateResponse


class ConsumersActivateRequest(TrenergyRequest):
    __api_path__ = "consumers/{consumer_id}/activate"
    __response__ = ConsumersActivateResponse
    __rest_method__ = RestMethod.POST

    consumer_id: int = Field(json_schema_extra=PATH_LOCATION)
