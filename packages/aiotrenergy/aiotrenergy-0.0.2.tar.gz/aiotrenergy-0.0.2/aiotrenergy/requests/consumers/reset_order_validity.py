from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import PATH_LOCATION
from aiotrenergy.responses.consumers.reset_order_validity import ConsumersResetOrderValidityResponse


class ConsumersResetOrderValidityRequest(TrenergyRequest):
    __api_path__ = "consumers/{consumer_id}/reset-validity"
    __response__ = ConsumersResetOrderValidityResponse
    __rest_method__ = RestMethod.PATCH

    consumer_id: int = Field(json_schema_extra=PATH_LOCATION)
