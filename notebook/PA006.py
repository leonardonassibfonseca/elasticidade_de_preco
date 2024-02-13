import pandas                 as pd
import numpy                  as np
import streamlit              as st
from matplotlib import pyplot as plt

# Importando os arquivos
path = '/home/leonardo/projetos_/elasticidade_de_preco/dataset'
df_elasticidade = pd.read_csv(path + '/df_elasticidade.csv')
df_resultado_negocio = pd.read_csv(path + '/df_resultado_negocio.csv')
df_resultado_negocio = df_resultado_negocio.drop('Unnamed: 0', axis = 1)

########## Layout Streamlit ##########
st.set_page_config(layout = 'wide')
st.header('Elasticidade de preços dos produtos')

tab1, tab2 = st.tabs(['Elasticidade de Preços', 'Resultado do Negócio'])

with tab1:
    # Apresentar elasticidade de preços
    tab3, tab4 = st.tabs(['Gráfico', 'Tabela'])
    with tab3:
        # Apresentar gráfico
        df_elasticidade['ranking'] = df_elasticidade.loc[:, 'elasticidade_de_preco'].rank(ascending = False).astype(int)
        df_elasticidade.reset_index(drop = True)
        fig, ax = plt.subplots()
        plt.figure(figsize = (17, 10))
        ax.hlines(y = df_elasticidade['nome'], xmin = 0, xmax = df_elasticidade['media_de_preco'], alpha = 0.5, linewidth = 6, color = 'red')
        st.pyplot(fig)
    with tab4:
        # Apresentar tabela
        df_elasticidade_ordenada = (df_elasticidade[['ranking', 'nome', 'elasticidade_de_preco']].drop_duplicates()
                                                                                                 .sort_values('elasticidade_de_preco', ascending = False))
        df_elasticidade_ordenada
        
    st.header('Elasticidade de Preços')
    st.dataframe(df_elasticidade, use_container_width = True)
    
with tab2:
    # Apresentar o resultado do negócio
    st.header('Resultado do Negócio')
    df_resultado_negocio = df_resultado_negocio.set_index('nome')
    st.dataframe(df_resultado_negocio, use_container_width = True)


