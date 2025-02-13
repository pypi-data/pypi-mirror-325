import datetime
import decimal

from aiotrenergy.enums import ConsumptionType
from aiotrenergy.objects.wallet import Wallet
from aiotrenergy.requests import (
    ConsumersIndexRequest,
    ConsumersCreateRequest,
    ConsumersShowRequest,
    ConsumersActivateRequest,
    ConsumersDeactivateRequest,
    ConsumersUpdateRequest,
    ConsumersDestroyRequest,
    ConsumersToggleAutoRenewalRequest,
    ConsumersBlockchainEnergyRequest,
    ConsumersMassTopUpTrxRequest,
    ConsumersActivateAddressRequest,
    ConsumersResetOrderValidityRequest,
    StoreDelayedConsumersRequest,
    ConsumersSummaryRequest,
    ConsumersAddressReportRequest,
    ConsumptionStatsRequest)
from aiotrenergy.responses import (
    ConsumersIndexResponse,
    ConsumersCreateResponse,
    ConsumersShowResponse,
    ConsumersActivateResponse,
    ConsumersDeactivateResponse,
    ConsumersUpdateResponse,
    ConsumersDestroyResponse,
    ConsumersToggleAutoRenewalResponse,
    ConsumersBlockchainEnergyResponse,
    ConsumersMassTopUpTrxResponse,
    ConsumersActivateAddressResponse,
    ConsumersResetOrderValidityResponse,
    StoreDelayedConsumersResponse,
    ConsumersSummaryResponse,
    ConsumersAddressReportResponse,
    ConsumptionStatsResponse)




class Consumers:
    def __init__(self, client):
        self.client = client

    async def index(self, per_page: int = None, page: int = None) -> ConsumersIndexResponse:
        request = ConsumersIndexRequest(per_page=per_page, page=page)
        return await request.emit(self.client)

    async def download(self):
        raise NotImplementedError

    async def create(
            self,
            payment_period: int,
            address: str,
            auto_renewal: bool,
            consumption_type: ConsumptionType,
            resource_amount: int,
            name: str,
            webhook_url: str = None
    ) -> ConsumersCreateResponse:
        request = ConsumersCreateRequest(
            payment_period=payment_period,
            address=address,
            auto_renewal=auto_renewal,
            consumption_type=consumption_type,
            resource_amount=resource_amount,
            name=name,
            webhook_url=webhook_url
        )
        return await request.emit(self.client)

    async def show(self, consumer_id: int) -> ConsumersShowResponse:
        request = ConsumersShowRequest(consumer_id=consumer_id)
        return await request.emit(self.client)

    async def activate(self, consumer_id: int) -> ConsumersActivateResponse:
        request = ConsumersActivateRequest(consumer_id=consumer_id)
        return await request.emit(self.client)

    async def deactivate(self, consumer_id: int) -> ConsumersDeactivateResponse:
        request = ConsumersDeactivateRequest(consumer_id=consumer_id)
        return await request.emit(self.client)

    async def update(
            self,
            consumer_id: int,
            name: str = None,
            payment_period: int = None,
            auto_renewal: bool = None,
            consumption_type: ConsumptionType = None,
            resource_amount: int = None
    ) -> ConsumersUpdateResponse:
        request = ConsumersUpdateRequest(
            consumer_id=consumer_id,
            name=name,
            payment_period=payment_period,
            auto_renewal=auto_renewal,
            consumption_type=consumption_type,
            resource_amount=resource_amount
        )
        return await request.emit(self.client)

    async def destroy(self, consumer_id: int) -> ConsumersDestroyResponse:
        request = ConsumersDestroyRequest(consumer_id=consumer_id)
        return await request.emit(self.client)

    async def toggle_auto_renewal(self, auto_renewal: bool, consumers: list[int]) -> ConsumersToggleAutoRenewalResponse:
        request = ConsumersToggleAutoRenewalRequest(auto_renewal=auto_renewal, consumers=consumers)
        return await request.emit(self.client)

    async def consumer_blockchain_energy(self, consumer_id: int) -> ConsumersBlockchainEnergyResponse:
        request = ConsumersBlockchainEnergyRequest(consumer_id=consumer_id)
        return await request.emit(self.client)

    async def mass_top_up_trx(self, amount: int, consumers: list[int]) -> ConsumersMassTopUpTrxResponse:
        request = ConsumersMassTopUpTrxRequest(amount=amount, consumers=consumers)
        return await request.emit(self.client)

    async def activate_address(self, address: str) -> ConsumersActivateAddressResponse:
        request = ConsumersActivateAddressRequest(address=address)
        return await request.emit(self.client)

    async def reset_order_validity(self, consumer_id: int) -> ConsumersResetOrderValidityResponse:
        request = ConsumersResetOrderValidityRequest(consumer_id=consumer_id)
        return await request.emit(self.client)

    async def store_delayed_consumers(
            self,
            webhook_url: str,
            deadline_at: datetime.datetime,
            wallets: list[Wallet]
    ) -> StoreDelayedConsumersResponse:
        request = StoreDelayedConsumersRequest(
            webhook_url=webhook_url,
            deadline_at=deadline_at,
            wallets=wallets
        )
        return await request.emit(self.client)

    async def consumers_summary(self) -> ConsumersSummaryResponse:
        request = ConsumersSummaryRequest()
        return await request.emit(self.client)

    async def address_report(
            self,
            address: str,
            from_date: datetime.date = None,
            to_date: datetime.date = None
    ) -> ConsumersAddressReportResponse:
        request = ConsumersAddressReportRequest(address=address, from_date=from_date, to_date=to_date)
        return await request.emit(self.client)

    async def consumption_stats(
            self,
            from_date: datetime.date,
            to_date: datetime.date,
            per_page: int = None,
            page: int = None
    ) -> ConsumptionStatsResponse:
        request = ConsumptionStatsRequest(
            from_date=from_date,
            to_date=to_date,
            per_page=per_page,
            page=page
        )
        return await request.emit(self.client)




