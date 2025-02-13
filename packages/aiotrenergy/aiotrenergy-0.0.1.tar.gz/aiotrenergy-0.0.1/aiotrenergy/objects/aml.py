import decimal

from pydantic import Field

from aiotrenergy.objects.base import TrenergyObject


class Aml(TrenergyObject):
    address: str
    txid: str | None
    context: 'AmlContext'


class AmlContext(TrenergyObject):
    pending: bool
    risk_score: decimal.Decimal | None = Field(alias='riskScore')
    entities: list['AmlEntity']


class AmlEntity(TrenergyObject):
    level: str
    entity: str
    risk_score: decimal.Decimal = Field(alias='riskScore')


AmlContext.model_rebuild()
Aml.model_rebuild()
