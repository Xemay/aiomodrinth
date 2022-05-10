from datetime import datetime
from abc import ABC, abstractmethod


def string_to_datetime(date: str, format_: str = None) -> datetime:
    if format_ is None:
        format_ = "%Y/%m/%d %H:%M:%S.%f"
    dt = datetime.strptime(date.replace('-', '/').replace('T', ' ').replace('Z', ''), format_)
    return dt


