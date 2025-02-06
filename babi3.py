# Adicionar ao código existente, após a seção Studio

with tabs[2]:  # Novo tab Decision Make
    st.title("🤖 Decision Make")
    st.subheader("Tomada de Decisão Automatizada")
    
    decision_type = st.selectbox(
        "Qual ação tomar?",
        ["Explorar Novos Mercados", "Ajustar Campanha", "Melhorar Produto"]
    )

    if decision_type == "Explorar Novos Mercados":
        st.markdown("### Análise de Expansão")
        
        # Dados simulados
        market_data = pd.DataFrame({
            'mercado': ['Digital', 'Skincare', 'Bem-estar'],
            'potencial': [0.8, 0.6, 0.9],
            'concorrencia': [0.7, 0.4, 0.3]
        })
        
        # Visualização
        fig = px.scatter(market_data, 
                        x='concorrencia', 
                        y='potencial',
                        text='mercado',
                        size=[40]*3)
        st.plotly_chart(fig)
        
        st.info("Recomendação: Explorar mercado de Bem-estar devido alto potencial e baixa concorrência")

    elif decision_type == "Ajustar Campanha":
        st.markdown("### Otimização de Campanha")
        
        metrics = {
            'Atual': [0.8, 0.4, 0.6],
            'Meta': [0.9, 0.6, 0.8]
        }
        
        fig = go.Figure(data=[
            go.Scatterpolar(r=metrics['Atual'], 
                           theta=['Engajamento', 'Conversão', 'ROI'],
                           name='Atual'),
            go.Scatterpolar(r=metrics['Meta'],
                           theta=['Engajamento', 'Conversão', 'ROI'],
                           name='Meta')
        ])
        st.plotly_chart(fig)
        
        st.info("Recomendação: Focar em aumentar taxa de conversão através de ofertas personalizadas")

    else:  # Melhorar Produto
        st.markdown("### Análise de Produto")
        
        feedback = pd.DataFrame({
            'aspecto': ['Embalagem', 'Fragrância', 'Textura', 'Preço'],
            'satisfacao': [4.2, 3.8, 4.5, 3.5]
        })
        
        fig = px.bar(feedback, x='aspecto', y='satisfacao',
                    title="Satisfação por Aspecto")
        st.plotly_chart(fig)
        
        st.info("Recomendação: Priorizar melhorias no preço e fragrância para aumentar satisfação")
