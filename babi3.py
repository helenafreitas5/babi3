import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import streamlit.components.v1 as components
import numpy as np

st.set_page_config(layout="wide", page_title="Plataforma IC Natura")

COMPETITORS = ["O Boticário", "Avon", "Eudora", "MAC", "Quem disse Berenice"]
TERRITORIES = ["Digital", "Sustentabilidade", "Experiência", "Inovação"] 
CATEGORIES = ["Skincare", "Makeup", "Perfumes", "Corpo", "Rosto"]

def generate_mock_data():
   movements = pd.DataFrame({
       'data': pd.date_range(start='2024-01-01', end='2024-02-04', freq='D'),
       'empresa': np.random.choice(COMPETITORS, 35),
       'territorio': np.random.choice(TERRITORIES, 35),
       'categoria': np.random.choice(CATEGORIES, 35),
       'relevancia': np.random.randint(1, 6, 35),
       'tipo': np.random.choice(['BAU', 'Bomba', 'Ninja'], 35, p=[0.7, 0.2, 0.1]),
       'engajamento': np.random.randint(100, 10000, 35),
       'descricao': np.random.choice([
           "Lançamento de nova linha",
           "Campanha nas redes sociais",
           "Parceria com influenciador", 
           "Expansão de mercado",
           "Programa de fidelidade",
           "Inovação em produto",
           "Ação sustentável"
       ], 35)
   })
   return movements

def zaia_widget():
   widget_html = """
       <div>
           <script>
               window.Widget = {
                   AgentURL: "https://platform.zaia.app/embed/chat/36828",
               };
           </script>
           <script src="https://platform.zaia.app/script/widget-loader.js"></script>
       </div>
   """
   components.html(widget_html, height=700)

movements_data = generate_mock_data()

st.title("🎯 Plataforma IC Natura")

tabs = st.tabs(["📊 Dashboard", "🔍 Fonte de Dados", "🤖 Decision Make", "📈 Studio"])

# Dashboard Tab
with tabs[0]:
   st.subheader("Overview de Mercado")
   
   col1, col2, col3, col4 = st.columns(4)
   with col1: st.metric("Movimentos", len(movements_data), "+3")
   with col2: st.metric("Ações Bomba", len(movements_data[movements_data['tipo'] == 'Bomba']), "+1")
   with col3: st.metric("Relevância Média", f"{movements_data['relevancia'].mean():.1f}", "+0.2")
   with col4: st.metric("Engajamento Total", f"{movements_data['engajamento'].sum():,}", "+12%")

   col1, col2 = st.columns(2)
   with col1:
       fig = px.bar(movements_data['territorio'].value_counts().reset_index(),
                   x='territorio', y='count', title="Movimentos por Território")
       st.plotly_chart(fig, use_container_width=True)
   
   with col2:
       fig = px.pie(movements_data['tipo'].value_counts().reset_index(),
                   values='count', names='tipo', title="Distribuição por Tipo de Ação")
       st.plotly_chart(fig, use_container_width=True)

# Fonte de Dados Tab
with tabs[1]:
   st.subheader("Fontes de Dados")
   
   col1, col2, col3 = st.columns(3)
   with col1:
       selected_competitor = st.multiselect("Empresas", COMPETITORS, default=COMPETITORS[:2])
   with col2:
       selected_territory = st.multiselect("Territórios", TERRITORIES, default=TERRITORIES[:2])
   with col3:
       date_range = st.date_input("Período", [datetime.now() - timedelta(days=30), datetime.now()])
       
   filtered_data = movements_data[
       (movements_data['empresa'].isin(selected_competitor)) &
       (movements_data['territorio'].isin(selected_territory))
   ]
   
   for _, movement in filtered_data.iterrows():
       with st.expander(f"{movement['data'].strftime('%d/%m/%Y')} - {movement['empresa']}: {movement['descricao']}"):
           col1, col2 = st.columns([3,1])
           with col1:
               st.markdown(f"**Território:** {movement['territorio']}")
               st.markdown(f"**Categoria:** {movement['categoria']}")
               st.markdown(f"**Engajamento:** {movement['engajamento']:,}")
           with col2:
               if movement['tipo'] == 'Bomba':
                   st.error(movement['tipo'])
               elif movement['tipo'] == 'Ninja':
                   st.warning(movement['tipo'])
               else:
                   st.info(movement['tipo'])
               st.metric("Relevância", movement['relevancia'])

# Decision Make Tab
with tabs[2]:
   st.title("🤖 Decision Make")
   st.subheader("Tomada de Decisão Automatizada")
   
   decision_type = st.selectbox("Qual ação tomar?",
                              ["Explorar Novos Mercados", "Ajustar Campanha", "Melhorar Produto"])

   if decision_type == "Explorar Novos Mercados":
       st.markdown("### Análise de Expansão")
       market_data = pd.DataFrame({
           'mercado': ['Digital', 'Skincare', 'Bem-estar'],
           'potencial': [0.8, 0.6, 0.9],
           'concorrencia': [0.7, 0.4, 0.3]
       })
       fig = px.scatter(market_data, x='concorrencia', y='potencial',
                       text='mercado', size=[40]*3)
       st.plotly_chart(fig)
       st.info("Recomendação: Explorar mercado de Bem-estar devido alto potencial e baixa concorrência")

   elif decision_type == "Ajustar Campanha":
       st.markdown("### Otimização de Campanha")
       metrics = {
           'Atual': [0.8, 0.4, 0.6],
           'Meta': [0.9, 0.6, 0.8]
       }
       fig = go.Figure(data=[
           go.Scatterpolar(r=metrics['Atual'], theta=['Engajamento', 'Conversão', 'ROI'],
                          name='Atual'),
           go.Scatterpolar(r=metrics['Meta'], theta=['Engajamento', 'Conversão', 'ROI'],
                          name='Meta')
       ])
       st.plotly_chart(fig)
       st.info("Recomendação: Focar em aumentar taxa de conversão através de ofertas personalizadas")

   else:
       st.markdown("### Análise de Produto")
       feedback = pd.DataFrame({
           'aspecto': ['Embalagem', 'Fragrância', 'Textura', 'Preço'],
           'satisfacao': [4.2, 3.8, 4.5, 3.5]
       })
       fig = px.bar(feedback, x='aspecto', y='satisfacao',
                   title="Satisfação por Aspecto")
       st.plotly_chart(fig)
       st.info("Recomendação: Priorizar melhorias no preço e fragrância para aumentar satisfação")

# Studio Tab        
with tabs[3]:
   st.subheader("Data Studio")
   analysis_type = st.selectbox("Tipo de Análise",
                              ["Quick Analysis", "Competitive Report", "Territory Deep Dive"])

   if analysis_type == "Quick Analysis":
       col1, col2 = st.columns(2)
       with col1:
           fig = px.scatter(movements_data, x='data', y='empresa',
                          size='relevancia', color='tipo', title="Timeline de Ações")
           st.plotly_chart(fig, use_container_width=True)
       with col2:
           territory_matrix = pd.crosstab(movements_data['empresa'], movements_data['territorio'])
           fig = px.imshow(territory_matrix, title="Heatmap de Territórios")
           st.plotly_chart(fig, use_container_width=True)

   elif analysis_type == "Competitive Report":
       st.markdown("### Análise Competitiva")
       for competitor in COMPETITORS[:3]:
           comp_data = movements_data[movements_data['empresa'] == competitor]
           st.markdown(f"#### {competitor}")
           col1, col2, col3 = st.columns(3)
           with col1:
               st.metric("Ações", len(comp_data))
           with col2:
               st.metric("Relevância Média", f"{comp_data['relevancia'].mean():.1f}")
           with col3:
               st.metric("% Ações Relevantes",
                        f"{(len(comp_data[comp_data['relevancia'] >= 4]) / len(comp_data) * 100):.1f}%")

   else:
       selected_territory = st.selectbox("Território", TERRITORIES)
       territory_data = movements_data[movements_data['territorio'] == selected_territory]
       col1, col2 = st.columns(2)
       with col1:
           fig = px.bar(territory_data['empresa'].value_counts().reset_index(),
                       x='empresa', y='count', title=f"Ações em {selected_territory}")
           st.plotly_chart(fig, use_container_width=True)
       with col2:
           fig = px.bar(territory_data.groupby('empresa')['relevancia'].mean().reset_index(),
                       x='empresa', y='relevancia', title=f"Relevância Média em {selected_territory}")
           st.plotly_chart(fig, use_container_width=True)

# Sidebar
with st.sidebar:
   st.header("Configurações")
   st.subheader("Fontes de Dados")
   
   # Simplified sources handling
   sources = ["Google Trends", "LinkedIn", "Notícias", "Redes Sociais"]
   for source in sources:
       if st.checkbox(source, value=True):
           st.success("✓")
       else:
           st.warning("×")
   
   st.subheader("Alertas")
   st.checkbox("Alertas de Bomba", value=True)
   st.checkbox("Alertas de Ninja", value=True)
   alert_relevance = st.slider("Relevância mínima", 1, 5, 4)

# Footer
st.markdown("---")
st.markdown(
   f"""<div style='text-align: center'>
       <small>Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M')} | 
       Powered by Zaia AI</small>
   </div>""",
   unsafe_allow_html=True
)
