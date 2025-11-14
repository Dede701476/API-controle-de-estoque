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

