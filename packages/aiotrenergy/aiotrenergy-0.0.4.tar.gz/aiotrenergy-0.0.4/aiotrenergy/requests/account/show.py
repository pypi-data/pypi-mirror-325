from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.responses.account.show import AccountShowResponse


class AccountShowRequest(TrenergyRequest):
    __api_path__ = "account"
    __response__ = AccountShowResponse
    __rest_method__ = RestMethod.GET
