"""Agente de análise de imagens médicas com Gemini Pro."""

from agno.agent import Agent
from agno.models.google import Gemini

from src.config.settings import settings
from src.agents.prompts import MEDICAL_ANALYSIS_PROMPT


def create_medical_agent() -> Agent:
    """Cria e retorna o agente de análise médica configurado."""
    return Agent(
        model=Gemini(id=settings.MODEL_NAME, api_key=settings.GOOGLE_API_KEY),
        instructions=[MEDICAL_ANALYSIS_PROMPT],
        markdown=True,
    )
