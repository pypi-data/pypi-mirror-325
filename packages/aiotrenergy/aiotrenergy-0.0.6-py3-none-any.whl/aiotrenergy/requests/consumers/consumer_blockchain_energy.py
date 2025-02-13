from pydantic import Field

from aiotrenergy.enums import RestMethod
from aiotrenergy.requests.base import TrenergyRequest
from aiotrenergy.requests.params import PATH_LOCATION
from aiotrenergy.responses.consumers.consumer_blockchain_energy import ConsumersBlockchainEnergyResponse


class ConsumersBlockchainEnergyRequest(TrenergyRequest):
    __api_path__ = "consumers/{consumer_id}/blockchain-energy"
    __response__ = ConsumersBlockchainEnergyResponse
    __rest_method__ = RestMethod.GET

    consumer_id: int = Field(json_schema_extra=PATH_LOCATION)
