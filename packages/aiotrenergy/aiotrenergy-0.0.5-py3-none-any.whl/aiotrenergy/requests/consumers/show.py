from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import PATH_LOCATION
from aiotrenergy.responses.consumers.show import ConsumersShowResponse


class ConsumersShowRequest(TrenergyRequest):
    __api_path__ = "consumers/{consumer_id}"
    __response__ = ConsumersShowResponse
    __rest_method__ = RestMethod.GET

    consumer_id: int = Field(json_schema_extra=PATH_LOCATION)