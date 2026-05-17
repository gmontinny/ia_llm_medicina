"""CLI para análise de imagens médicas com Gemini Pro."""

import sys
from agno.media import Image as AgnoImage

from src.agents.medical_agent import create_medical_agent
from src.utils.image_utils import validate_image, list_images, get_image_info
from src.config.settings import settings


def main():
    """Ponto de entrada da aplicação CLI."""
    print("=" * 60)
    print("🏥  Sistema de Análise de Imagens Médicas com IA")
    print("=" * 60)

    # Listar imagens disponíveis
    images = list_images(settings.IMAGES_DIR)

    if not images:
        print("❌ Nenhuma imagem encontrada na pasta 'laudo/'.")
        sys.exit(1)

    print("\n📁 Imagens disponíveis:")
    for i, img in enumerate(images, 1):
        info = get_image_info(img)
        print(f"  {i}. {img.split(chr(92))[-1]} ({info['size'][0]}x{info['size'][1]})")

    # Seleção
    try:
        choice = int(input("\n🔢 Selecione o número da imagem: ")) - 1
        if choice < 0 or choice >= len(images):
            raise ValueError
    except (ValueError, KeyboardInterrupt):
        print("❌ Seleção inválida.")
        sys.exit(1)

    image_path = images[choice]

    if not validate_image(image_path):
        print("❌ Arquivo inválido.")
        sys.exit(1)

    # Análise
    print("\n🔍 Analisando imagem...")
    agent = create_medical_agent()
    response = agent.run(
        "Analise esta imagem médica de forma detalhada.",
        images=[AgnoImage(filepath=image_path)],
    )

    print("\n📋 Resultado da Análise:")
    print("-" * 60)
    print(response.content)
    print("-" * 60)


if __name__ == "__main__":
    main()
