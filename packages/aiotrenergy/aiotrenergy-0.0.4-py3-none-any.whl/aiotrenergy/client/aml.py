from aiotrenergy.enums import Blockchain
from aiotrenergy.requests.aml.create import AmlCreateRequest
from aiotrenergy.requests.aml.index import AmlIndexRequest
from aiotrenergy.responses.aml.create import AmlCreateResponse
from aiotrenergy.responses.aml.index import AmlIndexResponse


class Aml:
    def __init__(self, client):
        self.client = client

    async def index(self, per_page: int = None, page: int = None) -> AmlIndexResponse:
        request = AmlIndexRequest(per_page=per_page, page=page)
        return await request.emit(self.client)

    async def create(self, blockchain: Blockchain, address: str = None, txid: str = None) -> AmlCreateResponse:
        request = AmlCreateRequest(blockchain=blockchain, address=address, txid=txid)
        return await request.emit(self.client)
