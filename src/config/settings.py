"""Módulo de configuração do projeto."""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Configurações centralizadas do projeto."""

    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "gemini-2.5-flash")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.3"))
    IMAGES_DIR: str = os.path.join(os.path.dirname(__file__), "..", "..", "laudo")


settings = Settings()
