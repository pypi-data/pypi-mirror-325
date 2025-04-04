from pathlib import Path
from typing import Union
from PIL import Image
from commons_imaging.image_info import ImageInfo


def get_image_info(filepath: Union[str, Path]) -> ImageInfo:
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"File {filepath} not found")

    try:
        with Image.open(filepath) as img:
            return ImageInfo(
                file_size=filepath.stat().st_size,
                format=img.format,
                width=img.width,
                height=img.height,
            )
    except IOError as e:
        raise IOError(f"Error opening file {filepath}: {e}")
