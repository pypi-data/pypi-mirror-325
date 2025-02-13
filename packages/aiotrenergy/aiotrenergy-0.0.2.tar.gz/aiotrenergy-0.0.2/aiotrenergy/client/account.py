from aiotrenergy.requests.account.show import AccountShowRequest
from aiotrenergy.requests.account.top_up import TopUpRequest
from aiotrenergy.responses.account.show import AccountShowResponse
from aiotrenergy.responses.account.top_up import TopUpResponse


class Account:
    def __init__(self, client):
        self.client = client

    async def show(self) -> AccountShowResponse:
        request = AccountShowRequest()
        return await request.emit(self.client)

    async def top_up(self) -> TopUpResponse:
        request = TopUpRequest()
        return await request.emit(self.client)
