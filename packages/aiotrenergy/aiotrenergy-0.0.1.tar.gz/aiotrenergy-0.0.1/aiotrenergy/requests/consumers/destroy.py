from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import PATH_LOCATION
from aiotrenergy.responses.consumers.destroy import ConsumersDestroyResponse


class ConsumersDestroyRequest(TrenergyRequest):
    __api_path__ = "consumers/{consumer_id}"
    __response__ = ConsumersDestroyResponse
    __rest_method__ = RestMethod.DELETE

    consumer_id: int = Field(json_schema_extra=PATH_LOCATION)
