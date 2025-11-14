from fastapi import FastAPI
import funcao as fun

app = FastAPI(title="Gerência de Produtos")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo á gerencia de produtos"}

@app.get("/adicionar")
def adicionar_produtos(nome: str, categoria: str, valor: float, quantidade: int):
    fun.adicionar_produtos(nome, categoria, valor, quantidade)
    return{"mensagem" : "produto adicionado!"}