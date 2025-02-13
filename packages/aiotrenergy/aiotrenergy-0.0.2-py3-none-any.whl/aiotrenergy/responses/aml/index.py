from aiotrenergy.objects.aml import Aml
from aiotrenergy.responses.pagination import TrenergyPaginationResponse


class AmlIndexResponse(TrenergyPaginationResponse[Aml]):
    pass