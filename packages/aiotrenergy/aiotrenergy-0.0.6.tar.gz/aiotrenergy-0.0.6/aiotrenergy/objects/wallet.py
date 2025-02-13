from aiotrenergy.objects.base import TrenergyObject


class Wallet(TrenergyObject):
    address: str
    energy_amount: int
    activate: bool
