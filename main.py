import os
import requests
from mcp.server.fastmcp import FastMCP

# Cria a ponte MCP
mcp = FastMCP("Meu App do AI Studio")

# Coloque as credenciais do seu app publicado
APP_URL = "https://jogo-de-tabuleiro-com-dados.ai.studio"
API_KEY = os.environ.get("AIzaSyALvrJvjKOGdCTa5BS8f3aCKrhfDjngffE")

@mcp.tool()
def perguntar_ao_meu_app(mensagem: str) -> str:
    """Envia uma mensagem para o aplicativo publicado e retorna a resposta."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    dados = {"prompt": mensagem}
    
    # Faz a chamada para o seu aplicativo publicado
    resposta = requests.post(APP_URL, json=dados, headers=headers)
    
    if resposta.status_code == 200:
        return resposta.json().get("texto", "Sem resposta")
    return "Erro ao consultar o aplicativo."

if __name__ == "__main__":
    mcp.run()
