from dataclasses import dataclass
from typing import Any

@dataclass(kw_only=True)
class Message:
    """Class for keeping track of messages."""
    Raw: bytes
    From: str
    To: str
    Parameters: dict | None = None
    Reply: bytes | Any
    error: str | None = None
    decoded: Any = None
    is_decoded: bool = False
    uid: str
    _source: str = ""
    _content_type: str = "application/json"

