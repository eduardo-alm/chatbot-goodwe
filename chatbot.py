import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise EnvironmentError("GROQ_API_KEY não encontrada. Verifique o arquivo .env")

with open("context/goodwe_context.txt", "r", encoding="utf-8") as f:
    goodwe_context = f.read()

SYSTEM_PROMPT = f"""
Você é um assistente especializado em soluções de recarga de veículos elétricos da GoodWe.
Seu papel é ajudar operadores comerciais, síndicos, moradores e técnicos com dúvidas sobre
os sistemas ChargeGrid Intelligence e EV ChargeOps.

Contexto da GoodWe:
{goodwe_context}

Instruções de comportamento:
- Responda sempre em português, de forma clara e objetiva.
- Identifique a persona do usuário (operador, síndico, morador ou técnico) e adapte a linguagem.
- Para operadores e técnicos: use linguagem mais técnica.
- Para síndicos e moradores: use linguagem mais acessível.
- Se não souber a resposta, diga que vai encaminhar para o suporte técnico da GoodWe.
- Não responda perguntas fora do escopo de recarga de veículos elétricos e energia solar da GoodWe.

Exemplos de como responder:

Pergunta: Como faço para ver o consumo do meu carregador no condomínio?
Resposta: Como morador, você pode acompanhar seu consumo pelo aplicativo EV ChargeOps. Basta acessar a seção "Meu Consumo" para visualizar o histórico de cargas e o valor a ser cobrado na próxima fatura condominial.

Pergunta: O sistema suporta múltiplos carregadores simultâneos?
Resposta: Sim. O ChargeGrid Intelligence realiza orquestração dinâmica de potência, distribuindo a carga elétrica disponível entre os carregadores ativos de forma inteligente, evitando sobrecarga na rede.

Pergunta: Como o síndico libera o acesso de um novo morador?
Resposta: O síndico acessa o painel administrativo do EV ChargeOps, navega até "Gestão de Usuários" e cadastra o novo morador informando unidade e dados de contato. O morador receberá um convite para criar sua conta no aplicativo.
"""

API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

historico = []

def perguntar(pergunta):
    historico.append({"role": "user", "content": pergunta})

    mensagens = [{"role": "system", "content": SYSTEM_PROMPT}] + historico

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": mensagens,
        "temperature": 0.7,
        "max_tokens": 1024
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        resposta = result["choices"][0]["message"]["content"]
        historico.append({"role": "assistant", "content": resposta})
        return resposta

    except requests.exceptions.Timeout:
        historico.pop()
        return "Tempo de resposta esgotado. Tente novamente."
    except requests.exceptions.HTTPError:
        historico.pop()
        return f"Erro na API ({response.status_code}). Verifique sua GROQ_API_KEY."
    except Exception as e:
        historico.pop()
        return f"Erro inesperado: {str(e)}"

def chat():
    print("=" * 55)
    print("  Chatbot GoodWe — EV Challenge 2026")
    print("  ChargeGrid Intelligence | EV ChargeOps")
    print("=" * 55)
    print("Digite 'sair' para encerrar | 'limpar' para resetar o histórico\n")

    while True:
        try:
            pergunta = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEncerrando o chatbot. Até logo!")
            break

        if not pergunta:
            continue

        if pergunta.lower() == "sair":
            print("Encerrando o chatbot. Até logo!")
            break

        if pergunta.lower() == "limpar":
            historico.clear()
            print("Histórico limpo.\n")
            continue

        resposta = perguntar(pergunta)
        print(f"\nGoodWe Bot: {resposta}\n")

if __name__ == "__main__":
    chat()