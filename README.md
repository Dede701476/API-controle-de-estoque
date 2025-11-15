# README

Este projeto integra um back-end desenvolvido com FastAPI a um front-end criado em streamlit, permitindo que a interface web consuma dados fornecidos pela API. O back-end pode se comunicar com um banco PostgreSQL utilizando variáveis de ambiente definidas em um arquivo .env.

# Tecnologias Utilizadas
FastAPI, Streamlit, Uvicorn, PostgreSQL, psycopg2, psycopg2-binary, Requests, python-dotenv e dotenv.

# Instalação
Para instalar, você pode opcionalmente criar um ambiente virtual usando:
python -m venv venv
source venv/bin/activate   (Linux/Mac)
venv\Scripts\activate      (Windows)
Depois, instale as dependências com:
pip install -r requirements.txt

# Configuração
Crie um arquivo .env dentro da pasta do backend com as seguintes variáveis:
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=SUA_SENHA
DB_NAME=SEU_BANCO
Essas variáveis são usadas para conectar ao banco PostgreSQL.

# Como Executar o Backend (FastAPI)
Dentro da pasta "backend", execute:
uvicorn main:app --reload --port 8000
A API ficará disponível e a documentação automática pode ser acessada em:
http://localhost:8000/docs

# Como Executar o Frontend (Streamlit)
Dentro da pasta "frontend", execute:
streamlit run app.py
O navegador abrirá automaticamente exibindo a interface da aplicação.

# Fluxo da Aplicação
O usuário acessa o Streamlit, que envia requisições HTTP para o FastAPI usando a biblioteca Requests. O FastAPI processa os dados e quando necessário acessa o banco PostgreSQL. O resultado retorna ao Streamlit, que exibe as informações ao usuário.

# Requirements
dotenv==0.9.9
fastapi==0.121.2
psycopg2==2.9.11
psycopg2-binary==2.9.11
python-dotenv==1.2.1
requests==2.32.5
streamlit==1.51.0
uvicorn==0.38.0

# Licença
Projeto livre para uso acadêmico.
