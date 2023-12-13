import streamlit as st
import pandas as pd

def main():
    st.title("Carregador de Arquivo CSV")

    # Carregando o arquivo CSV
    uploaded_file = st.file_uploader("Carregar arquivo CSV", type=['csv'])

    if uploaded_file is not None:
        # Lendo o arquivo CSV
        df = pd.read_csv(uploaded_file)

        # Exibindo o conteúdo do arquivo carregado
        st.write("Conteúdo do Arquivo:")
        st.write(df)

if __name__ == "__main__":
    main()
