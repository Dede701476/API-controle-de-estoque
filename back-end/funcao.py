from conexao import conector



#----------------CRIAR TABELA-----------------|


def criar_tabela_produtos():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    categoria VARCHAR(50),
                    preco DECIMAL(10,2),
                    quantidade INT
                );
            """)
            conexao.commit()
            print("Tabela 'produtos' criada com sucesso!")
        except Exception as erro:
            print(f"Erro ao criar a tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela_produtos()

#-----------------ADICIONAR-----------------|


def adicionar_produtos(nome, categoria, preco, quantidade):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
                INSERT INTO produtos (nome, categoria, preco, quantidade)
                VALUES  (%s, %s, %s, %s)
            """, (nome, categoria, preco, quantidade))
            conexao.commit()
            print("Produto adicionado com sucesso!")
        except Exception as erro:
            print(f"Erro ao adicionar produto, erro: {erro}")
        finally:
            cursor.close()
            conexao.close()

adicionar_produtos("produto", "categoria", 00, 10)

#-----------------LISTAR-----------------|

def listar_produtos():
    conexao, cursor = conector()

    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY id",
                
            )
            return cursor.fetchall()
        
        except Exception as erro:
            print(f"Erro ao tentar exbir produtos: {erro}")
            return []
        
        finally:
            cursor.close()
            conexao.close()

    else:
        print("Não foi possivel listar os produtos tente novamente mais tarde!")

#----------------atualizar------------------|

def atualizar_item(id, novo_preco, nova_quantia):
    conexao, cursor = conector() 
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET preco = %s, quantidade = %s WHERE id = %s",
                (novo_preco, nova_quantia, id)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print("Produto atualizado com sucesso!")
            else:
                print("Nenhum produto encontrado com esse ID.")
        except Exception as erro:
            print(f"Erro ao tentar atualizar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

#----------------Deletar------------------|

def deletar_produto(id):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s",
                (id,)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print("Produto removido do carrinho com sucesso!")
            else:
                print("Nenhum Produto foi encontrado em nosso estoque.")
        except Exception as erro:
            print(f"Erro ao tentar inserir produtos: {erro}")
        finally:
            cursor.close()
            conexao.close()

#-----------------Buscar---------------|

def buscar_produto(id_produto):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos WHERE id = %s",
                (id_produto,)
            )
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao buscar o produto: {erro}")
        finally:
            cursor.close()
            conexao.close()





