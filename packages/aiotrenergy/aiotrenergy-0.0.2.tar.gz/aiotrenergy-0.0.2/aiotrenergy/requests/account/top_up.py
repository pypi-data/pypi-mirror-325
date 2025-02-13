from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.responses.account.top_up import TopUpResponse


class TopUpRequest(TrenergyRequest):
    __api_path__ = "account/top-up"
    __response__ = TopUpResponse
    __rest_method__ = RestMethod.GET
