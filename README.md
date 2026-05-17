# 🏥 IA LLM Medicina - Análise de Imagens Médicas

Sistema de apoio diagnóstico que utiliza o modelo **Gemini 3 Pro** (Google) para análise inteligente de imagens médicas como radiografias, tomografias e ressonâncias.

## 📋 Funcionalidades

- Análise automatizada de imagens médicas com IA multimodal
- Identificação do tipo de exame e região anatômica
- Listagem de achados relevantes
- Avaliação diagnóstica com diagnósticos diferenciais
- Explicação em linguagem acessível ao paciente
- Interface web (Streamlit) e CLI

## 🏗️ Estrutura do Projeto

```
ia_llm_medicina/
├── src/
│   ├── agents/
│   │   ├── medical_agent.py   # Agente de análise com Gemini
│   │   └── prompts.py         # Prompts estruturados
│   ├── config/
│   │   └── settings.py        # Configurações centralizadas
│   └── utils/
│       └── image_utils.py     # Utilitários de imagem
├── laudo/                      # Imagens médicas para análise
├── notebook/                   # Notebook original de referência
├── app.py                      # Interface Streamlit
├── main.py                     # Interface CLI
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## 🚀 Como Executar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar variáveis de ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env` com sua chave da API do Google:

```env
GOOGLE_API_KEY=sua_chave_aqui
MODEL_NAME=gemini-3-pro-preview
TEMPERATURE=0.3
```

### 3. Executar a interface web

```bash
streamlit run app.py
```

### 4. Executar via CLI

```bash
python main.py
```

## 🐳 Docker

### Build e execução com Docker Compose

```bash
docker compose up --build
```

A aplicação estará disponível em `http://localhost:8501`.

### Apenas build da imagem

```bash
docker build -t ia-medicina .
docker run -p 8501:8501 --env-file .env -v ./laudo:/app/laudo ia-medicina
```

> O volume `./laudo` é montado para adicionar/remover imagens sem rebuild.

## 🛠️ Tecnologias

- **Gemini 3 Pro** - Modelo multimodal do Google para análise de imagens
- **Agno** - Framework para criação de agentes de IA
- **google-genai** - SDK oficial do Google para API Gemini
- **Streamlit** - Interface web interativa
- **Pillow** - Manipulação de imagens
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **Docker** - Containerização da aplicação

## 🔧 Modelos Disponíveis

O modelo pode ser alterado no `.env`. Opções compatíveis:

| Modelo | Descrição |
|--------|-----------|
| `gemini-3-pro-preview` | Mais avançado, melhor para análises complexas |
| `gemini-2.5-flash` | Rápido e eficiente |
| `gemini-2.5-pro` | Equilíbrio entre qualidade e velocidade |

Referência: [Documentação Google Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-pro)

## ⚠️ Aviso

Este sistema é **apenas para fins educacionais e de pesquisa**. Não substitui a avaliação de um profissional médico qualificado.
