from typing_extensions import TypeVar, Generic

from pydantic import BaseModel, field_validator

T = TypeVar('T', default=None)


class TrenergyResponse(BaseModel, Generic[T]):
    data: T | None = None

    @field_validator("data", mode="before")
    def check_data(cls, v):
        if v == {}:
            return None
        return v
