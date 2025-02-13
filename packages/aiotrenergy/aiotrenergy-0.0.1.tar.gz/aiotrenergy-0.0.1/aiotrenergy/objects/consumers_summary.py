import decimal

from aiotrenergy.objects.base import TrenergyObject


class ConsumersSummary(TrenergyObject):
    balance: decimal.Decimal
    credit_limit: int
    total_count: int
    total_energy_consumption: int
    total_received_energy: int
    active_count: int
    active_energy_consumption: int
    normal_energy_unit_price: decimal.Decimal
    trenergy_energy_unit_price: decimal.Decimal
    aml_price_usd: int
    daily_expenses_avg: decimal.Decimal
