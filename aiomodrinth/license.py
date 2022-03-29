from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class License:
    id: str
    name: str
    url: str | None
