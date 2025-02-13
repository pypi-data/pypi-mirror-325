import datetime

from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.pagination import TrenergyPaginationRequest
from aiotrenergy.requests.params import QUERY_LOCATION
from aiotrenergy.responses.consumers.consumption_stats import ConsumptionStatsResponse


class ConsumptionStatsRequest(TrenergyPaginationRequest):
    __api_path__ = "consumers/consumption-stats"
    __response__ = ConsumptionStatsResponse
    __rest_method__ = RestMethod.GET

    from_date: datetime.date = Field(json_schema_extra=QUERY_LOCATION)
    to_date: datetime.date = Field(json_schema_extra=QUERY_LOCATION)
