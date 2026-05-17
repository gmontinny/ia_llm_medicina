"""Utilitários para manipulação de imagens médicas."""

import os
from pathlib import Path

from PIL import Image

SUPPORTED_FORMATS = (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp")


def validate_image(path: str) -> bool:
    """Valida se o arquivo é uma imagem suportada."""
    return Path(path).suffix.lower() in SUPPORTED_FORMATS and os.path.isfile(path)


def get_image_info(path: str) -> dict:
    """Retorna informações básicas da imagem."""
    img = Image.open(path)
    return {
        "path": path,
        "size": img.size,
        "mode": img.mode,
        "format": img.format,
    }


def list_images(directory: str) -> list[str]:
    """Lista todas as imagens em um diretório."""
    if not os.path.isdir(directory):
        return []
    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if Path(f).suffix.lower() in SUPPORTED_FORMATS
    ]
