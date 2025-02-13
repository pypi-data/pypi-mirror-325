from typing import Awaitable
from .utils.to_async import to_async
from ..packages import PackagesService
from ...models import ListPackagesOkResponse


class PackagesServiceAsync(PackagesService):
    """
    Async Wrapper for PackagesServiceAsync
    """

    def list_packages(
        self,
        destination: str = None,
        start_date: str = None,
        end_date: str = None,
        after_cursor: str = None,
        limit: float = None,
        start_time: int = None,
        end_time: int = None,
        duration: float = None,
    ) -> Awaitable[ListPackagesOkResponse]:
        return to_async(super().list_packages)(
            destination,
            start_date,
            end_date,
            after_cursor,
            limit,
            start_time,
            end_time,
            duration,
        )
