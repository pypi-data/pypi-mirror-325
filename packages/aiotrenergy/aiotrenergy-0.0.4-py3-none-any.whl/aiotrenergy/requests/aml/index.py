from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.pagination import TrenergyPaginationRequest
from aiotrenergy.responses.aml.index import AmlIndexResponse


class AmlIndexRequest(TrenergyPaginationRequest):
    __api_path__ = "aml"
    __response__ = AmlIndexResponse
    __rest_method__ = RestMethod.GET
