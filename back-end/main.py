from fastapi import FastAPI
import funcao as fun

app = FastAPI(title="Gerência de Produtos")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo á gerencia de produtos"}