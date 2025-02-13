from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.responses.consumers.consumers_summary import ConsumersSummaryResponse


class ConsumersSummaryRequest(TrenergyRequest):
    __api_path__ = "consumers/summary"
    __response__ = ConsumersSummaryResponse
    __rest_method__ = RestMethod.GET