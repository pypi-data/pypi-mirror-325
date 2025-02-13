from aiotrenergy.objects.consumer import Consumer
from aiotrenergy.responses.pagination import TrenergyPaginationResponse


class ConsumersIndexResponse(TrenergyPaginationResponse[Consumer]):
    pass