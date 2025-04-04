from dataclasses import dataclass


@dataclass
class ImageInfo:
    format: str
    width: int
    height: int
    file_size: int
