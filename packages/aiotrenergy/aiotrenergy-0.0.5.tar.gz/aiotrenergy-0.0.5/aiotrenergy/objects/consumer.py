import datetime
from typing import Annotated

from pydantic import Field, BeforeValidator

from .base import TrenergyObject
from ..enums import CreationType, ConsumptionType, OrderStatus


datetime_field = Annotated[datetime.datetime, BeforeValidator(lambda x: datetime.datetime.strptime(x, "%d-%m-%Y %H:%M:%S"))]


class Order(TrenergyObject):
    status: OrderStatus
    completion_percentage: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    valid_until: datetime.datetime


class Consumer(TrenergyObject):
    id: int
    name: str
    address: str
    resource_amount: int
    creation_type: CreationType
    consumption_type: ConsumptionType
    payment_period: int
    auto_renewal: bool
    resource_consumptions: int | None = None
    is_active: bool
    order: Order | None = None
    boost_order: Order | None = Field(None, alias='boostOrder')
    webhook_url: str | None
    created_at: datetime_field
    updated_at: datetime_field
