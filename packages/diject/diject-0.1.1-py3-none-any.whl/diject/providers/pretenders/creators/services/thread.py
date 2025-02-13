import logging
import threading
from typing import Any, Callable, Final, Generic, Iterator, Type, TypeVar

from diject.extensions.scope import Scope
from diject.extensions.shutdown import ShutdownProtocol
from diject.extensions.status import Status, StatusProtocol
from diject.providers.pretenders.creators.services.service import (
    ServicePretenderBuilder,
    ServiceProvider,
)
from diject.utils.exceptions import DIAsyncError
from diject.utils.lock import Lock

T = TypeVar("T")

LOG = logging.getLogger(__name__)


class ThreadData(Generic[T]):
    def __init__(
        self,
        data: tuple[Iterator[T] | T, T],
        on_close: Callable[[Iterator[T] | T], None],
    ) -> None:
        self.data = data
        self.on_close = on_close

    def __del__(self) -> None:
        obj, _ = self.data
        self.on_close(obj)


class ThreadProvider(ServiceProvider[T], StatusProtocol, ShutdownProtocol):
    def __init__(
        self,
        callable: Callable[..., Iterator[T]] | Type[T] | Callable[..., T],
        /,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(callable, *args, **kwargs)
        self.__lock = Lock()
        self.__thread_data = threading.local()

    def __provide__(self, scope: Scope | None = None) -> T:
        with self.__lock:
            return self.__provide()

    async def __aprovide__(self, scope: Scope | None = None) -> T:
        async with self.__lock:
            try:
                return self.__provide()
            except DIAsyncError:
                LOG.critical(_msg := f"'{self}' cannot provide asynchronous services")
                raise DIAsyncError(_msg)

    def __provide(self) -> T:
        if not hasattr(self.__thread_data, "objects"):
            self.__thread_data.objects = ThreadData(
                data=self.__create_object_and_instance__(),
                on_close=self.__close_object__,
            )

        _, instance = self.__thread_data.objects.data
        return instance

    def __status__(self) -> Status:
        return Status.STOPPED if hasattr(self.__thread_data, "objects") else Status.STARTED

    def __shutdown__(self, only_current_thread: bool = False) -> None:
        with self.__lock:
            if only_current_thread:
                if hasattr(self.__thread_data, "objects"):
                    delattr(self.__thread_data, "objects")
            else:
                del self.__thread_data
                self.__thread_data = threading.local()

    async def __ashutdown__(self, only_current_thread: bool = False) -> None:
        async with self.__lock:
            if only_current_thread:
                if hasattr(self.__thread_data, "objects"):
                    delattr(self.__thread_data, "objects")
            else:
                del self.__thread_data
                self.__thread_data = threading.local()


Thread: Final = ServicePretenderBuilder(ThreadProvider)
