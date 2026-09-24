import os
import requests
from mcp.server.mcpserver import MCPServer

# Cria a ponte MCP com a versao atualizada
mcp = MCPServer("Meu App do AI Studio")

APP_URL = "https://jogo-de-tabuleiro-com-dados.ai.studio"
API_KEY = os.environ.get("AIzaSyALvrJvjKOGdCTa5BS8f3aCKrhfDjngffE", "")

@mcp.tool()
def perguntar_ao_meu_app(mensagem: str) -> str:
    """Envia uma mensagem para o aplicativo publicado e retorna a resposta."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    dados = {"prompt": mensagem}
    
    resposta = requests.post(APP_URL, json=dados, headers=headers)
    
    if resposta.status_code == 200:
        return resposta.json().get("texto", "Sem resposta")
    return "Erro ao consultar o aplicativo."

if __name__ == "__main__":
    # Inicia a ponte escutando a porta que o Render precisa
    porta = int(os.environ.get("PORT", 8000))
    mcp.run(transport="sse", host="0.0.0.0", port=porta)
