import requests

# Endereço da API
url = "http://127.0.0.1:8000/usuarios"

print(f"Conectando ao servidor em: {url}...")

try:
    # Consumindo o endpoint via HTTP GET
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        print("\n--- Dados recebidos da API Python ---")
        for usuario in dados:
            print(f"ID: {usuario['id']} | Nome: {usuario['nome']} | Cargo: {usuario['cargo']}")
    else:
        print(f"Erro no servidor: {response.status_code}")

except Exception as e:
    print(f"Erro ao tentar consumir a API: {e}")