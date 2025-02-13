import datetime
from typing import Annotated

from pydantic import HttpUrl, Field, AfterValidator, BeforeValidator

from aiotrenergy.objects.base import TrenergyObject

datetime_field = Annotated[datetime.datetime, BeforeValidator(lambda x: datetime.datetime.strptime(x, "%d-%m-%Y %H:%M:%S"))]


class Account(TrenergyObject):
    name: str
    email: str
    lang: str
    the_code: str
    invitation_code: str | None = None
    credit_limit: int
    leader_name: str | None = None
    leader_level: int
    consumer_level: int | None = None
    is_banned: bool
    balance_restricted: bool
    photo: HttpUrl
    balance: int
    reinvestment: str | None = None
    stakes_sum: int
    stakes_profit: int
    reactors_count: int
    two_fa: bool = Field(alias="2fa")
    created_at: datetime_field
    updated_at: datetime_field
    deletion_at: datetime_field | None = None