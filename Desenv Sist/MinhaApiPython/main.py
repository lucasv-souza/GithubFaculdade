from fastapi import FastAPI

app = FastAPI()

# Endpoint que retorna dados fictícios de usuários
@app.get("/usuarios")
def get_usuarios():
    return [
        {"id": 1, "nome": "Lucas Vinicius", "cargo": "Desenvolvedor"},
        {"id": 2, "nome": "Daniel Lima", "cargo": "Professor"},
        {"id": 3, "nome": "João", "cargo": "Estudante"}
    ]