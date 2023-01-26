
#============================================
# Libraries
#============================================

from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go
import inflection

#============================================
# Bibliotecas necessárias
#============================================

import folium
import pandas as pd
import streamlit as st
from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static

#============================================
#  Ajustar tela para wide
#============================================

st.set_page_config(page_title="Cuisines", page_icon="🍽️", layout="wide")

#============================================
# Funções
#============================================

# 1. De-Para-Países

COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

#--------------------------------------------

def country_name(country_id):
    return COUNTRIES[country_id]

# 2. De-Para tipo de comida

def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"
    
#--------------------------------------------

# 3. DE-Para Cores:

COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

def color_name(color_code):
    return COLORS[color_code]

#--------------------------------------------

# 4. Renomeando Colunas

def rename_columns(dataframe):
    
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

#--------------------------------------------

# 5. Tratando os Dados

def clean_code( df1 ):   

    # 1. Removendo Linhas Duplicadas

    #df1 = df1.drop_duplicates(keep='first')
    df1 = df1.drop_duplicates()

    # 2. Renomeando Colunas

    df1 = rename_columns( df1 )

    # 3. Criando a Coluna País

    df1["country"] = df1.loc[:, "country_code"].apply( lambda x: country_name(x) )

    # 4. Categoraizando as comidas

    df1['food_category'] = df1.loc[:, 'price_range'].apply( lambda x: create_price_tye( x ) )

    # 5. Colocando nome as cores

    df1['color_name'] = df1.loc[:, 'rating_color'].apply( lambda x: color_name( x ) )

    # 6. Categorizando tipo de restaurantes por 1 tipo de culinária

    df1['cuisines'] = df1['cuisines'].astype(str)
    df1['cuisines'] = df1.loc[:, 'cuisines'].apply( lambda x: x.split(",")[0] )

    # 7. Excluindo colunas que votação é zerada

    #df1 = df1.loc[ df1['votes'] > 0, :]

    # 8. Excluindo colunas que votação é zerada

    df1 = df1.loc[ df1['cuisines'] != 'nan', :]

    # 9. Eliminando a possibilidade de ter espaços nas colunas Texto/ object(trim)
    # df1.dtypes

    df1.loc[:, 'restaurant_name'] = df1.loc[:, 'restaurant_name'].str.strip()
    df1.loc[:, 'city'] = df1.loc[:, 'city'].str.strip()
    df1.loc[:, 'address'] = df1.loc[:, 'address'].str.strip()
    df1.loc[:, 'locality'] = df1.loc[:, 'locality'].str.strip()
    df1.loc[:, 'locality_verbose'] = df1.loc[:, 'locality_verbose'].str.strip()
    df1.loc[:, 'cuisines'] = df1.loc[:, 'cuisines'].str.strip()
    df1.loc[:, 'currency'] = df1.loc[:, 'currency'].str.strip()
    df1.loc[:, 'rating_color'] = df1.loc[:, 'rating_color'].str.strip()
    df1.loc[:, 'rating_text'] = df1.loc[:, 'rating_text'].str.strip()
    df1.loc[:, 'country'] = df1.loc[:, 'country'].str.strip()
    df1.loc[:, 'food_category'] = df1.loc[:, 'food_category'].str.strip()
    df1.loc[:, 'color_name'] = df1.loc[:, 'color_name'].str.strip()
    
    return( df1 )

#--------------------------------------------

# 6. Montando os KPI's
    
def melhores_restaurantes_nome_nota( df, culinaria, coluna ):

        df_aux = ( df.loc[ df['cuisines'] == culinaria,
                  ['restaurant_id','restaurant_name','country','city','cuisines','average_cost_for_two',
                   'aggregate_rating','votes']]   
        .sort_values(['aggregate_rating','restaurant_id'], ascending=[False,True])
        .iloc[0,:].to_dict())
        
        df_aux = df_aux.get(coluna)
        
        return df_aux     
    
#--------------------------------------------

# 7. Melhores Culinárias
   
def melhores_culinarias( df1 ):
    
        linhas_selecionadas = df1['country'].isin(filtro_paises)

        df_aux = (df1.loc[linhas_selecionadas, ['cuisines','aggregate_rating']].groupby(['cuisines']).mean()
            .sort_values(['aggregate_rating'], 
                         ascending=False).reset_index().head(restaurant_slider))

        fig = px.bar(df_aux,
              x='cuisines',
              y='aggregate_rating',
              text='aggregate_rating',
              text_auto='.2f',
              title='Top 10 Melhores Tipos de Culinárias',
              labels={
                  'cuisines':'Tipo de Culinária',
                  'aggregate_rating':'Média da Avaliação Média'        }
              )


        fig = fig.update_layout(title_text=f'Top {restaurant_slider} Melhores Tipos de Culinárias', title_x=0.5)
        
        return fig
    
#--------------------------------------------

# 8. Piores Culinárias
   
def piores_culinarias( df1 ):        
    
    linhas_selecionadas = df1['country'].isin(filtro_paises)
    
    df_aux = (df1.loc[linhas_selecionadas, ['cuisines','aggregate_rating']].groupby(['cuisines']).mean()
            .sort_values(['aggregate_rating'], 
                         ascending=True).reset_index())

    #Tratando a coluna que agr tem um média calculada
    df_aux = df_aux.loc[ df_aux['aggregate_rating'] > 0, :].head(restaurant_slider)

    fig = px.bar(df_aux,
          x='cuisines',
          y='aggregate_rating',
          text='aggregate_rating',
          text_auto='.2f',
          title='Top 10 Piores Tipos de Culinárias',
          labels={
              'cuisines':'Tipo de Culinária',
              'aggregate_rating':'Média da Avaliação Média'}
          )


    fig = fig.update_layout(title_text=f'Top {restaurant_slider} Piores Tipos de Culinárias', title_x=0.5)
        
    return fig


#-------------------------------------------- 


#============================================
# Importar Dataset
#============================================

#df = pd.read_csv(r'C:\Users\israelguastalle-sao\repos_cds\FTC\projeto_final\dataset\zomato.csv')
#df1 = clean_code( df )
#df2 = df1.copy()

#============================================
# Importar Para Cloud
#============================================

df = pd.read_csv( 'dataset/zomato.csv' )
df1 = clean_code( df )
df2 = df1.copy()

#============================================
# BARRA LATERAL NO STREAMLIT
#============================================

#============================================
# FILTROS
#============================================

st.sidebar.markdown('## Filtros:')
st.sidebar.markdown('Escolha os Países que deseja visualizar nas análises:')


#----- Criando filro de Países -----

filtro_paises = st.sidebar.multiselect('Quais Países?',
                                        df1.loc[:, 'country'].unique().tolist(),
                                        default = ['Brazil','England','Qatar','South Africa','Canada','Australia'])


#----- Criando filro Qtd. Restaurantes ----

restaurant_slider = st.sidebar.slider(
    'Selecione a quantidade de Restaurantes que deseja visualizar:',
    value = 10,
    min_value = 1,
    max_value = 20)


#----- Criando filro Culinárias -----

filtro_culinaria = st.sidebar.multiselect('Escolha os Tipos de Culinária:',
                                        df1.loc[:, 'cuisines'].unique().tolist(),
                                        default = ['Home-made','BBQ','Japanese','Brazilian','Arabian','American','Italian'])


#-----Ativando o filtro de Países -----

linhas_selecionadas = df1['country'].isin( filtro_paises )
df1 = df1.loc[linhas_selecionadas, :]

#-----Ativando o filtro Qtd. Restaurantes-----


#---


#-----Ativando o filtro Culinárias -----


linhas_selecionadas2 = df1['cuisines'].isin( filtro_culinaria )
df1 = df1.loc[linhas_selecionadas2, :]


#-------------------------------------

st.sidebar.markdown("""---""")
st.sidebar.markdown('Powered by Israel Guastalle')

#============================================
# LAYOUT NO STREAMLIT
#============================================

st.markdown('## 🍽️ Visão Culinária')

#---------Primeira Linha-----------

with st.container():

    st.markdown('### Melhores Restaurantes dos Principais Tipos Culinários:')
    
    col1, col2, col3 = st.columns(3, gap='large')
    
    with col1:    
        
        st.markdown("""---""")
           
        #df_aux1 = melhores_restaurantes_nome_nota( df2, 'Italian', 'cuisines'  )
        df_aux2 = melhores_restaurantes_nome_nota( df2, 'Italian', 'aggregate_rating'  )
        df_aux3 = melhores_restaurantes_nome_nota( df2, 'Italian', 'restaurant_name'  )
        
        st.markdown(f'###### 🍽️ Itália: {df_aux3}')
        st.markdown(f'###### ❤️ Nota: {df_aux2} / 5.0')     
        #st.markdown(f'###### Restaurante: {df_aux3}')  
        
        st.markdown("""---""")
    
    with col2:
        
        st.markdown("""---""")
        
        #df_aux1 = melhores_restaurantes_nome_nota( df2, 'Italian', 'cuisines'  )
        df_aux2 = melhores_restaurantes_nome_nota( df2, 'American', 'aggregate_rating'  )
        df_aux3 = melhores_restaurantes_nome_nota( df2, 'American', 'restaurant_name'  )
        
        st.markdown(f'###### 🍽️ EUA: {df_aux3}')
        st.markdown(f'###### ❤️ Nota: {df_aux2} / 5.0')     
        #st.markdown(f'###### Restaurante: {df_aux3}') 
        
        st.markdown("""---""")
        
    with col3:
        
        st.markdown("""---""")
        
        #df_aux1 = melhores_restaurantes_nome_nota( df2, 'Italian', 'cuisines'  )
        df_aux2 = melhores_restaurantes_nome_nota( df2, 'Arabian', 'aggregate_rating'  )
        df_aux3 = melhores_restaurantes_nome_nota( df2, 'Arabian', 'restaurant_name'  )
        
        st.markdown(f'###### 🍽️ Árabe: {df_aux3}')
        st.markdown(f'###### ❤️ Nota: {df_aux2} / 5.0')     
        #st.markdown(f'###### Restaurante: {df_aux3}')  

        st.markdown("""---""")
    
#---------Segunda Linha------------

with st.container():
   
    col1, col2, col3 = st.columns(3, gap='large')
           
    with col1:
        #df_aux1 = melhores_restaurantes_nome_nota( df2, 'Italian', 'cuisines'  )
        df_aux2 = melhores_restaurantes_nome_nota( df2, 'Japanese', 'aggregate_rating'  )
        df_aux3 = melhores_restaurantes_nome_nota( df2, 'Japanese', 'restaurant_name'  )
        
        st.markdown(f'###### 🍽️ Japonesa: {df_aux3}')
        st.markdown(f'###### ❤️ Nota: {df_aux2} / 5.0')     
        #st.markdown(f'###### Restaurante: {df_aux3}')  
        
    with col2:
        #df_aux1 = melhores_restaurantes_nome_nota( df2, 'Italian', 'cuisines'  )
        df_aux2 = melhores_restaurantes_nome_nota( df2, 'Brazilian', 'aggregate_rating'  )
        df_aux3 = melhores_restaurantes_nome_nota( df2, 'Brazilian', 'restaurant_name'  )
        
        st.markdown(f'###### 🍽️ Brasil: {df_aux3}')
        st.markdown(f'###### ❤️ Nota: {df_aux2} / 5.0')     
        #st.markdown(f'###### Restaurante: {df_aux3}')  

    with col3:
        #df_aux1 = melhores_restaurantes_nome_nota( df2, 'Italian', 'cuisines'  )
        df_aux2 = melhores_restaurantes_nome_nota( df2, 'Chinese', 'aggregate_rating'  )
        df_aux3 = melhores_restaurantes_nome_nota( df2, 'Chinese', 'restaurant_name'  )
        
        st.markdown(f'###### 🍽️ China: {df_aux3}')
        st.markdown(f'###### ❤️ Nota: {df_aux2} / 5.0')     
        #st.markdown(f'###### Restaurante: {df_aux3}')  

    st.markdown("""---""")


#---------Terceira Linha------------

with st.container():

    st.markdown(f"## Top {restaurant_slider} Restaurantes")
    
    df_aux = ( df1.loc[:, ['restaurant_id','restaurant_name','country','city',
               'cuisines','average_cost_for_two','aggregate_rating','votes']]
        .sort_values(['aggregate_rating','restaurant_id'], ascending=[False,True]).head(restaurant_slider))

            
    #st.dataframe( df_aux width=1000,  height=500)   
    st.dataframe( df_aux, width=1000)


#---------Quarta Linha------------


with st.container():

    col1, col2 = st.columns(2, gap='large')
    
    with col1: 
    
        fig = melhores_culinarias( df2 )
        st.plotly_chart(fig, use_container_width=True)
        
    with col2: 
    
        fig = piores_culinarias( df2 )
        st.plotly_chart(fig, use_container_width=True)      
        
    
        
    





