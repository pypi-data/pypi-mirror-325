from datetime import datetime
from typing import Generic, TypeVar, Optional, List

from mag_tools.exception.app_exception import AppException
from mag_tools.model.service_status import ServiceStatus

T = TypeVar('T')

class Results(Generic[T]):
    def __init__(self, status: Optional[str] = None, code: Optional[str] = None, message: Optional[str] = None,
                 data: Optional[List[T]] = None, total_count: Optional[int] = None, timestamp: Optional[datetime] = None):
        self.status = ServiceStatus.of_code(status) if status else ServiceStatus.OK
        self.code = ServiceStatus.of_code(code) if code else ServiceStatus.OK
        self.message = message
        self.data = data if data else []
        self.total_count = total_count if total_count else len(self.data)
        self.timestamp = timestamp if timestamp else datetime.now()

    @staticmethod
    def exception(ex: Exception) -> 'Results':
        message = str(ex) if ex.args else str(ex.__cause__)
        return Results(status=ServiceStatus.INTERNAL_SERVER_ERROR.code, code=ServiceStatus.INTERNAL_SERVER_ERROR.code, message=message)

    @staticmethod
    def success(data: Optional[List[T]] = None) -> 'Results':
        return Results(message="OK", data=data)

    @staticmethod
    def fail(message: str) -> 'Results':
        return Results(code=ServiceStatus.INTERNAL_SERVER_ERROR.code, message=message)

    @property
    def is_success(self) -> bool:
        return self.status == ServiceStatus.OK.value and self.code == ServiceStatus.OK.value

    @property
    def size(self) -> int:
        return len(self.data)

    @property
    def first(self) -> Optional[T]:
        return self.data[0] if len(self.data) > 0 else None

    def check(self) -> None:
        if not self.is_success:
            raise AppException(self.message)

    def get(self, idx: int) -> Optional[T]:
        self.check()
        return self.data[idx] if idx < self.size else None

    def to_dict(self):
        return {
            'status': self.status.code,
            'code': self.code.code,
            'message': self.message,
            'timestamp': self.timestamp,
            'data': self.data,
            'total_count': self.total_count
        }