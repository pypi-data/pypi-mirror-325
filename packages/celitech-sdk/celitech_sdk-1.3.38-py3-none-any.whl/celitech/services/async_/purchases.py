from typing import Awaitable
from .utils.to_async import to_async
from ..purchases import PurchasesService
from ...models import (
    ListPurchasesOkResponse,
    CreatePurchaseOkResponse,
    CreatePurchaseRequest,
    TopUpEsimOkResponse,
    TopUpEsimRequest,
    EditPurchaseOkResponse,
    EditPurchaseRequest,
    GetPurchaseConsumptionOkResponse,
)


class PurchasesServiceAsync(PurchasesService):
    """
    Async Wrapper for PurchasesServiceAsync
    """

    def list_purchases(
        self,
        iccid: str = None,
        after_date: str = None,
        before_date: str = None,
        reference_id: str = None,
        after_cursor: str = None,
        limit: float = None,
        after: float = None,
        before: float = None,
    ) -> Awaitable[ListPurchasesOkResponse]:
        return to_async(super().list_purchases)(
            iccid,
            after_date,
            before_date,
            reference_id,
            after_cursor,
            limit,
            after,
            before,
        )

    def create_purchase(
        self, request_body: CreatePurchaseRequest
    ) -> Awaitable[CreatePurchaseOkResponse]:
        return to_async(super().create_purchase)(request_body)

    def top_up_esim(
        self, request_body: TopUpEsimRequest
    ) -> Awaitable[TopUpEsimOkResponse]:
        return to_async(super().top_up_esim)(request_body)

    def edit_purchase(
        self, request_body: EditPurchaseRequest
    ) -> Awaitable[EditPurchaseOkResponse]:
        return to_async(super().edit_purchase)(request_body)

    def get_purchase_consumption(
        self, purchase_id: str
    ) -> Awaitable[GetPurchaseConsumptionOkResponse]:
        return to_async(super().get_purchase_consumption)(purchase_id)
