# Read_Books

## Projeto CRUD com FastAPI, SQLAlchemy, Pydantic, PostgreSQL, Streamlit e Docker

# Visão Geral

Este projeto tem como objetivo criar uma aplicação CRUD utilizando FastAPI para o backend, SQLAlchemy para a interação com o banco de dados PostgreSQL, Pydantic para validação de dados, Streamlit para a interface web e Docker para containerização. FastAPI é um framework moderno e de alta performance para construção de APIs, enquanto Streamlit facilita a criação de dashboards e aplicações web interativas. Docker garante que o ambiente de desenvolvimento seja consistente e facilita a implantação em diferentes ambientes.

# Ferramentas e Tecnologias

Python: Linguagem de programação principal.
FastAPI: Framework moderno e de alta performance para construção de APIs.
SQLAlchemy: Biblioteca ORM (Object-Relational Mapping) para gerenciamento do banco de dados.
Pydantic: Biblioteca para validação de dados.
PostgreSQL: Banco de dados relacional robusto e escalável.
Uvicorn: Servidor ASGI para rodar a aplicação FastAPI.
Streamlit: Biblioteca para criação de interfaces web interativas.
Docker: Plataforma de containerização para criar, implantar e rodar aplicações em containers.
Poetry: Ferramenta para gerenciamento de dependências e empacotamento no Python.


## Diagrama da Estrutura do Projeto

```mermaid
graph TD
    A[Read_Books] --> B[Backend]
    B --> C[main.py]
    B --> D[models.py]
    B --> E[schemas.py]
    B --> F[crud.py]
    B --> G[database.py]
    B --> H[router.py]
    B --> I[Dockerfile]
    B --> J[.dockerignore]
    B --> K[requirements.txt]
    A --> L[docker-compose.yml]
    A --> M[.dockerignore]
    A --> N[.gitignore]
    A --> O[pyproject.toml]
    A --> P[poetry.lock]
    A --> Q[.python-version]
    A --> R[README.md]
````