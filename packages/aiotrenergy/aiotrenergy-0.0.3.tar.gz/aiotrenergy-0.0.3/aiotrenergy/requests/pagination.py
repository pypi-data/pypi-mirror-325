from abc import ABC

from pydantic import Field

from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import QUERY_LOCATION


class TrenergyPaginationRequest(TrenergyRequest, ABC):
    per_page: int | None = Field(None, json_schema_extra=QUERY_LOCATION)
    page: int | None = Field(None, json_schema_extra=QUERY_LOCATION)
