import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

with open("context/goodwe_context.txt", "r", encoding="utf-8") as f:
    goodwe_context = f.read()

SYSTEM_PROMPT = f"""
Você é um assistente especializado em soluções de recarga de veículos elétricos da GoodWe.
Seu papel é ajudar operadores comerciais, síndicos, moradores e técnicos com dúvidas sobre 
os sistemas ChargeGrid Intelligence e EV ChargeOps.

Contexto da GoodWe:
{goodwe_context}

Responda sempre em português, de forma clara e objetiva.
Se não souber a resposta, diga que vai encaminhar para o suporte técnico.
"""

API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def perguntar(pergunta):
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": pergunta}
        ]
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    result = response.json()
    return result["choices"][0]["message"]["content"]

def chat():
    print("Chatbot GoodWe iniciado! Digite 'sair' para encerrar.\n")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            break
        resposta = perguntar(pergunta)
        print(f"\nGoodWe Bot: {resposta}\n")

if __name__ == "__main__":
    chat()