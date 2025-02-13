import logging
from json import JSONDecodeError

import httpx
from httpx import AsyncClient, URL

from aiotrenergy.client.account import Account
from aiotrenergy.client.aml import Aml
from aiotrenergy.client.consumers import Consumers
from aiotrenergy.exceptions import NetworkError, HttpStatusError, TrenergyStatusError, raise_error, AiotrenergyException
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.responses.base import TrenergyResponse


class TrenergyClient:
    def __init__(
            self,
            api_key: str,
            base_url: str = "https://core.tr.energy/api/",
            *,
            httpx_client: AsyncClient = None,
    ):
        self.api_key = api_key
        self.base_url = URL(base_url).join(api_key)
        self.httpx_client = httpx_client or AsyncClient(http2=True)
        self.aml = Aml(self)
        self.account = Account(self)
        self.consumers = Consumers(self)

    async def close(self):
        await self.httpx_client.aclose()

    async def request(self, request: TrenergyRequest) -> TrenergyResponse:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = request.params()
        url = self.base_url.join(request.__api_path__.format(**params.path))
        try:
            response = await self.httpx_client.request(
                request.__rest_method__.value,
                url,
                headers=headers,
                json=params.body,
                params=params.query
            )
        except httpx.RequestError as e:
            raise NetworkError(e) from e

        try:
            result = response.json()
        except JSONDecodeError as e:
            try:
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                raise HttpStatusError(e) from e
            raise AiotrenergyException("Failed to decode JSON response") from e
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            raise_error(response.status_code, result)

        status = result.pop("status")
        if status is False:
            raise TrenergyStatusError

        return request.__response__.model_validate(result)
