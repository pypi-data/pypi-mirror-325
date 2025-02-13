from typing import TypeVar

from aiotrenergy.objects.base import TrenergyObject

TrenergyType = TypeVar("TrenergyType", bound=TrenergyObject)
