import datetime

from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import QUERY_LOCATION
from aiotrenergy.responses.consumers.address_report import ConsumersAddressReportResponse


class ConsumersAddressReportRequest(TrenergyRequest):
    __api_path__ = "consumers/address-report"
    __response__ = ConsumersAddressReportResponse
    __rest_method__ = RestMethod.GET

    address: str = Field(json_schema_extra=QUERY_LOCATION)
    from_date: datetime.date | None = Field(None, json_schema_extra=QUERY_LOCATION)
    to_date: datetime.date | None = Field(None, json_schema_extra=QUERY_LOCATION)
