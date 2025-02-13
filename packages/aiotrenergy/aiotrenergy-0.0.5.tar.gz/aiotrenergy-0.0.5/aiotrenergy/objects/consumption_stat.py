import decimal
import datetime

from aiotrenergy.objects.base import TrenergyObject


class ConsumptionStat(TrenergyObject):
    date: datetime.date
    resource_amount: int
    trx_price: decimal.Decimal
