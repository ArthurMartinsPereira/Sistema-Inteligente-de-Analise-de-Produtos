import streamlit as st

st.set_page_config(
    page_title="Product Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("Product Analytics")
st.subheader("Sistema de Análise de Produtos e Vendas")

st.write("Bem-vindo ao Product Analytics!")
st.info("Nossa aplicação está sendo desenvolvida.")

st.divider()

st.header("Visão Geral")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Produtos cadastrados", 0)

with col2:
    st.metric("Vendas realizadas", 0)

with col3:
    st.metric("Receita total", "R$ 0,00")