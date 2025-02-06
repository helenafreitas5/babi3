import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Natura Intelligence Hub",
    layout="wide"
)

menu = st.sidebar.selectbox(
    "Menu",
    ["Dashboard", "Monitoramento", "Reports", "Benchmarks", "AI Assistant"]
)

if menu == "Dashboard":
    st.title("Dashboard")
    
    # Métricas
    c1, c2 = st.columns(2)
    c1.metric("Ações", "223")
    c2.metric("Insights", "45")
    
    # Tabela exemplo
    data = {
        'Data': ['2024-02-06', '2024-02-05'],
        'Marca': ['Boticário', 'Eudora'],
        'Ação': ['Campanha Verão', 'Lançamento Perfume'],
        'Relevância': [4, 3]
    }
    st.dataframe(pd.DataFrame(data))

elif menu == "Monitoramento":
    st.title("Monitoramento")
    
    # Filtros
    marca = st.selectbox("Marca", ["Todos", "Boticário", "Eudora"])
    categoria = st.multiselect("Categoria", ["Perfumaria", "Presentes"])
    relevancia = st.slider("Relevância", 1, 4, 2)

else:
    st.title(menu)
