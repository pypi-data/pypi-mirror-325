from pydantic import HttpUrl, BaseModel, Field

from aiotrenergy.objects.base import TrenergyObject
from aiotrenergy.responses.base import TrenergyResponse
from aiotrenergy.types import TrenergyType


class TrenergyPaginationResponse(TrenergyResponse[list[TrenergyType]]):
    links: 'PaginationLinks'
    meta: 'PaginationMeta'


class PaginationLinks(TrenergyObject):
    first: HttpUrl
    last: HttpUrl
    prev: HttpUrl | None
    next: HttpUrl | None


class PaginationMeta(TrenergyObject):
    current_page: int
    from_: int | None = Field(alias="from")
    last_page: int
    links: list['PaginationMetaLink']
    path: HttpUrl
    per_page: int
    to: int | None
    total: int


class PaginationMetaLink(TrenergyObject):
    url: HttpUrl | None
    label: str
    active: bool


PaginationMeta.model_rebuild()
TrenergyPaginationResponse.model_rebuild()
