from fastapi import FastAPI
import funcao as fun

app = FastAPI(title="Gerência de Produtos")

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo á gerencia de produtos"}

#-------------|CRIAR|-------------

@app.post("/produtos")
def criar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    fun.adicionar_produtos(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto cadastrado com sucesso!"}

# #-------------|LISTAR|-------------

@app.get("/produtos")
def listar_produtos():
    produtos = fun.listar_produtos()
    lista = []

    for linha in produtos:
        lista.append({
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
        })
    
    return {"produtos": lista}

# #-------------|ATUALIZAR|-------------

@app.put("/produtos/{id_produto}")
def atualizar_produtos(id_produto: int, novo_preco: float, nova_quantidade: int):
    produto = fun.atualizar_item(id_produto, novo_preco, nova_quantidade)

    if produto:
        fun.atualizar_produtos(id_produto, novo_preco, nova_quantidade)
        return {"erro": "Produto não encontrado"}
    else:
        return {"mensagem": "Produto atualizado com sucesso!"}
    
#-------------|DELETAR|-------------

@app.delete("/produtos/{id_produto}")
def deletar_produtos(id_produto: int):
    produto = fun.buscar_produto(id_produto)

    if produto:
        fun.deletar_produto(id_produto)
        return {"mensagem": "Produto excluído com sucesso!"}
    else:
        return {"erro": "Produto não encontrado"}