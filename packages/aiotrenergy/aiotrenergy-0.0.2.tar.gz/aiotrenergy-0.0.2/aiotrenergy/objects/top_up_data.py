from pydantic import HttpUrl

from aiotrenergy.objects.base import TrenergyObject


class TopUpData(TrenergyObject):
    address: str
    qr_code: HttpUrl
    time_left: int = None
