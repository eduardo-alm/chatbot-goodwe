# Chatbot GoodWe — EV Challenge 2026

## Integrantes
| Nome | RM |
|---|---|
| Eduardo Oliveira | 570374 |
| Timoteo de Andrade Romano | 569711 |
| Bruno Albuquerque Aguiar | 569035 |
| João Pedro Conturbia | 569788 |
| Enzo De Nadai | 569985 |
| Leonardo Duarte | 569029 |

## Descrição
Chatbot com IA desenvolvido para auxiliar operadores, síndicos, moradores e técnicos com dúvidas sobre os sistemas ChargeGrid Intelligence e EV ChargeOps da GoodWe.

## Problema Abordado
A GoodWe enfrenta a ausência de mecanismos integrados nos eletropostos para:
- **ChargeGrid Intelligence**: orquestrar potência, registrar ciclos de carga, realizar faturamento e comunicação em eletropostos comerciais.
- **EV ChargeOps**: gerenciar uso compartilhado de carregadores em condomínios, com controle de acesso e faturamento individual por unidade.

## Justificativa da Escolha do Contexto
Optamos por atender ambos os contextos (comercial e condominial) pois o system prompt identifica a persona do usuário e direciona respostas específicas para cada cenário, tornando o chatbot mais versátil e operacionalmente útil.

## Tecnologias Utilizadas
- Python 3.14
- Groq API (LLaMA 3.1 8B Instant)
- python-dotenv

## Por que Groq + LLaMA 3.1?
- Gratuito e sem limitações de rede
- Rápido e eficiente para respostas em português
- Fácil integração via API REST
- Ideal para prototipagem rápida
- LLaMA 3.1 é open source, desenvolvido pela Meta, amplamente utilizado no mercado

## Personas Atendidas
- Operador comercial
- Síndico
- Morador
- Técnico

## Estrutura do Projeto
chatbot-goodwe/
├── chatbot.py
├── README.md
├── context/
│   └── goodwe_context.txt
└── docs/
    ├── fluxograma.png
    └── perguntas_teste.md

## Como Rodar
1. Clone o repositório
2. Crie o arquivo `.env` com sua chave: `GROQ_API_KEY=sua_chave`
3. Instale as dependências: `pip install requests python-dotenv`
4. Execute: `python chatbot.py`

## Fluxograma
![Fluxograma](docs/fluxograma.png)

## System Prompt
O contexto-base utilizado para condicionar o modelo está em `context/goodwe_context.txt` e é injetado no system prompt do chatbot a cada sessão.

## Modelo de Teste
Disponível em `docs/perguntas_teste.md` com 5 perguntas e respostas esperadas.