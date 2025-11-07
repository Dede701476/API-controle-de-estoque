from conexao import conector



#----------------'CRIAR TABELA-----------------|

def criar_tabela_produtos():
    conector = conector()
    if conector:
        try:
            cursor = conector.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    categoria VARCHAR(50),
                    preco DECIMAL(10,2),
                    quantidade INT
                );
            """)
            conector.commit()
            print("Tabela 'produtos' criada com sucesso!")
        except Exception as e:
            print("Erro ao criar a tabela:", e)
        finally:
            cursor.close()
            conector.close()

if __name__ == "__main__":
    criar_tabela_produtos()


