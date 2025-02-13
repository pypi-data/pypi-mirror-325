import decimal

from aiotrenergy.objects.consumption_stat import ConsumptionStat
from aiotrenergy.responses.pagination import TrenergyPaginationResponse


class ConsumptionStatsResponse(TrenergyPaginationResponse[ConsumptionStat]):
    total_trx_price: decimal.Decimal
    total_resource_amount: decimal.Decimal
    total_energy_balance_expenses: int
