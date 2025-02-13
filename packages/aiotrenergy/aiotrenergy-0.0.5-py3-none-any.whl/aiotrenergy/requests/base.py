import datetime
import decimal
from abc import abstractmethod, ABC
from typing import TYPE_CHECKING, Generic, TypeVar, Any

import pydantic
from pydantic import BaseModel

from aiotrenergy.enums import RestMethod
from aiotrenergy.responses.base import TrenergyResponse

if TYPE_CHECKING:
    from aiotrenergy.client.client import TrenergyClient


R = TypeVar("R", bound=TrenergyResponse)


@pydantic.dataclasses.dataclass
class Params:
    query: dict[str, Any]
    path: dict[str, Any]
    body: dict[str, Any]


class TrenergyRequest(BaseModel, Generic[R], ABC):
    # if TYPE_CHECKING:
    #     __api_path__: str
    #     __rest_method__: RestMethod
    #     __response__: R
    # else:
    @property
    @abstractmethod
    def __api_path__(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def __rest_method__(self) -> RestMethod:
        raise NotImplementedError

    @property
    @abstractmethod
    def __response__(self) -> R:
        raise NotImplementedError

    def params(self) -> Params:
        params = {
            "query": {},
            "path": {},
            "body": {},
        }
        serialized = self.model_dump(exclude_none=True, mode="json")
        for field_name, field_info in self.model_fields.items():
            location = field_info.json_schema_extra.get("location")
            if location:
                if location not in params:
                    raise ValueError(f"Unknown location: {location}")
                if field_name in serialized:
                    params[location][field_name] = serialized[field_name]
        return Params(**params)

    async def emit(self, client: 'TrenergyClient') -> R:
        return await client.request(self)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            RestMethod: lambda v: v.value,
            datetime.date: lambda v: f"{v:%Y-%m-%d}",
            datetime.datetime: lambda v: f"{v:%Y-%m-%d %H:%M}",
            decimal.Decimal: lambda v: int(str(v))
        }
        use_enum_values = True
