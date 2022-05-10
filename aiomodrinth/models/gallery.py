from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .utils import string_to_datetime


@dataclass
class GalleryImage:
    url: str
    featured: bool
    title: Optional[str]
    description: Optional[str]
    created: datetime

    @classmethod
    def fromlist(cls, images: list[dict]) -> list['GalleryImage']:
        imgs = []
        for i in images:
            imgs.append(GalleryImage.fromjson(**i))
        return imgs

    @classmethod
    def fromjson(cls, **kwargs):
        kwargs['created'] = string_to_datetime(kwargs['created'])
        return cls(**kwargs)
