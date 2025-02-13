from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.pagination import TrenergyPaginationRequest
from aiotrenergy.responses.consumers.index import ConsumersIndexResponse


class ConsumersIndexRequest(TrenergyPaginationRequest):
    __api_path__ = "consumers"
    __response__ = ConsumersIndexResponse
    __rest_method__ = RestMethod.GET
