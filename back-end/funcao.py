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
                "SELECT * FROM produtos ORDER BY ID"
            )
            return cursor.fetchall()      
        except Exception as erro:
            print(f"Erro ao tentar exbir produtos: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()
