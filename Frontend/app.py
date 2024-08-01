import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")
st.image("logo.png", width=100)
st.title("Gerenciamento de Livros")

# Função auxiliar para exibir mensagens de erro detalhadas
def show_response_message(response):
    if response.status_code == 200:
        st.success("Operação realizada com sucesso!")
    else:
        try:
            data = response.json()
            if "detail" in data:
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Erro: {errors}")
                else:
                    st.error(f"Erro: {data['detail']}")
        except ValueError:
            st.error("Erro desconhecido. Não foi possível decodificar a resposta.")

# Adicionar Livro
with st.expander("Adicionar um livro"):
    with st.form("new_book"):
        name = st.text_input("Nome do livro")
        category = st.text_input("Categoria")
        publisher = st.text_input("Editora")
        number_of_pages = st.number_input("Número de páginas")
        start_reading = st.date_input("Início da leitura", args=None, kwargs=None, format="YYYY-MM-DD")
        end_reading = st.date_input("Fim da leitura", args=None, kwargs=None, format="YYYY-MM-DD")
        submit_button = st.form_submit_button("Adicionar livro")

        if submit_button:
            response = requests.post(
                "http://backend:8000/books/",
                json={
                    "name": name,
                    "category": category,
                    "publisher": publisher,
                    "number_of_pages": number_of_pages,
                    "start_reading": start_reading.isoformat(),
                    "end_reading": end_reading.isoformat()
                }
            )
            show_response_message(response)

# Visualizar Livros
with st.expander("Visualizar livros"):
    if st.button("Exibir todos livros"):
        response = requests.get("http://backend:8000/books/")
        if response.status_code == 200:
            books = response.json()
            df = pd.DataFrame(books)

            expected_columns = [
                "id",
                "name",
                "category",
                "publisher",
                "number_of_pages",
                "start_reading",
                "end_reading",
                "created_at",
            ]

            # Filtrar apenas as colunas que existem no DataFrame
            available_columns = [col for col in expected_columns if col in df.columns]
            if available_columns:
                df = df[available_columns]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                st.error("Nenhuma coluna esperada encontrada no DataFrame.")
        else:
            show_response_message(response)

# Obter Detalhes de um Livro
with st.expander("Buscar livro"):
    get_id = st.number_input("ID do livro", min_value=1, format="%d")
    if st.button("Buscar"):
        response = requests.get(f"http://backend:8000/books/{get_id}")
        if response.status_code == 200:
            book = response.json()
            df = pd.DataFrame([book])

            expected_columns = [
                "id",
                "name",
                "category",
                "publisher",
                "number_of_pages",
                "start_reading",
                "end_reading",
                "created_at",
            ]

            # Filtrar apenas as colunas que existem no DataFrame
            available_columns = [col for col in expected_columns if col in df.columns]
            if available_columns:
                df = df[available_columns]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                st.error("Nenhuma coluna esperada encontrada no DataFrame.")
        else:
            show_response_message(response)

# Atualizar Livro
with st.expander("Atualizar livro"):
    with st.form("update_book"):
        update_id = st.number_input("ID do livro", min_value=1, format="%d")
        new_name = st.text_input("Novo nome do livro")
        new_category = st.text_area("Nova categoria do livro")
        new_publisher = st.text_area("Nova editora do livro")
        new_number_of_pages = st.number_input("Nova quantidade de páginas")
        new_start_reading = st.date_input("Nova data de início de leitura", args=None, kwargs=None, format="YYYY-MM-DD")
        new_end_reading = st.date_input("Nova data de fim de leitura", args=None, kwargs=None, format="YYYY-MM-DD")

        update_button = st.form_submit_button("Atualizar livro")

        if update_button:
            update_data = {}
            if new_name:
                update_data["name"] = new_name
            if new_category:
                update_data["category"] = new_category
            if new_publisher:
                update_data["publisher"] = new_publisher
            if new_number_of_pages:
                update_data["number_of_pages"] = new_number_of_pages
            if new_start_reading:
                update_data["start_reading"] = new_start_reading.isoformat()
            if new_end_reading:
                update_data["end_reading"] = new_end_reading.isoformat()  

            if update_data:
                response = requests.put(
                    f"http://backend:8000/books/{update_id}", json=update_data
                )
                show_response_message(response)
            else:
                st.error("Nenhuma informação fornecida para atualização")

# Deletar Livro
with st.expander("Deletar livro"):
    delete_id = st.number_input("ID do livro para deletar", min_value=1, format="%d")
    if st.button("Deletar livro"):
        response = requests.delete(f"http://backend:8000/books/{delete_id}")
        show_response_message(response)                
