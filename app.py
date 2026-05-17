"""Aplicação Streamlit para análise de imagens médicas com IA."""

import streamlit as st
from agno.media import Image as AgnoImage

from src.agents.medical_agent import create_medical_agent
from src.utils.image_utils import validate_image, list_images
from src.config.settings import settings


st.set_page_config(
    page_title="IA Medicina - Análise de Imagens",
    page_icon="🏥",
    layout="wide",
)

st.title("🏥 Análise de Imagens Médicas com IA")
st.markdown("Sistema de apoio diagnóstico utilizando **Gemini Pro** para análise de imagens médicas.")
st.divider()


@st.cache_resource
def get_agent():
    """Inicializa o agente (cache para não recriar a cada interação)."""
    return create_medical_agent()


def analyze_image(image_path: str) -> str:
    """Executa a análise da imagem médica."""
    agent = get_agent()
    response = agent.run(
        "Analise esta imagem médica de forma detalhada.",
        images=[AgnoImage(filepath=image_path)],
    )
    return response.content


# --- Sidebar ---
with st.sidebar:
    st.header("📁 Opções")
    source = st.radio("Origem da imagem:", ["Upload", "Pasta local (laudo/)"])

# --- Main ---
image_path = None

if source == "Upload":
    uploaded = st.file_uploader(
        "Envie uma imagem médica",
        type=["png", "jpg", "jpeg", "bmp", "tiff", "webp"],
    )
    if uploaded:
        temp_path = f"temp_{uploaded.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded.getbuffer())
        image_path = temp_path

else:
    images = list_images(settings.IMAGES_DIR)
    if images:
        selected = st.selectbox(
            "Selecione uma imagem:",
            images,
            format_func=lambda x: x.split("\\")[-1],
        )
        image_path = selected
    else:
        st.warning("Nenhuma imagem encontrada na pasta `laudo/`.")

# --- Exibição e Análise ---
if image_path and validate_image(image_path):
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(image_path, caption="Imagem selecionada", width="stretch")

    with col2:
        if st.button("🔍 Analisar Imagem", type="primary"):
            with st.spinner("Analisando imagem com Gemini Pro..."):
                try:
                    result = analyze_image(image_path)
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Erro na análise: {e}")

# --- Footer ---
st.divider()
st.caption("⚠️ Este sistema é apenas para fins educacionais. Não substitui avaliação médica profissional.")
