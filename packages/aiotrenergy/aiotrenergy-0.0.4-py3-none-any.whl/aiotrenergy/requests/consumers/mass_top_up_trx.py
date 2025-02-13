from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import BODY_LOCATION
from aiotrenergy.responses.consumers.mass_top_up_trx import ConsumersMassTopUpTrxResponse


class ConsumersMassTopUpTrxRequest(TrenergyRequest):
    __api_path__ = "consumers/mass/trx"
    __response__ = ConsumersMassTopUpTrxResponse
    __rest_method__ = RestMethod.POST

    amount: int = Field(..., le=100, json_schema_extra=BODY_LOCATION)
    consumers: list[int] = Field(..., json_schema_extra=BODY_LOCATION)