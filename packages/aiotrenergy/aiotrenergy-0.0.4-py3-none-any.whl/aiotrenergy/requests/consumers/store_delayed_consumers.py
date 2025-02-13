import datetime
from typing import Annotated

from pydantic import HttpUrl, Field, BeforeValidator

from aiotrenergy.enums import RestMethod
from aiotrenergy.objects.wallet import Wallet
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import BODY_LOCATION
from aiotrenergy.responses.consumers.store_delayed_consumers import StoreDelayedConsumersResponse

datetime_field = Annotated[datetime.datetime, BeforeValidator(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M"))]


class StoreDelayedConsumersRequest(TrenergyRequest):
    __api_path__ = "consumers/mass/delayed"
    __response__ = StoreDelayedConsumersResponse
    __rest_method__ = RestMethod.POST

    webhook_url: HttpUrl = Field(json_schema_extra=BODY_LOCATION)
    deadline_at: datetime.datetime = Field(json_schema_extra=BODY_LOCATION)
    wallets: list[Wallet] = Field(json_schema_extra=BODY_LOCATION)
