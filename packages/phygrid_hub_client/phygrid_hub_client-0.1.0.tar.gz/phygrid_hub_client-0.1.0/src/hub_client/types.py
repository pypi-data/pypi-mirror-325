from enum import Enum
from typing import Any, Dict, Optional, TypedDict

class TwinStatusEnum(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    UNKNOWN = "unknown"

class ScreenTwinReportedProperties(TypedDict, total=False):
    status: TwinStatusEnum
    data: Dict[str, Any]

class EventPayload(TypedDict, total=False):
    twin_id: Optional[str]
    status: Optional[TwinStatusEnum]
    data: Any