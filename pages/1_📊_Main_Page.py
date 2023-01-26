
#============================================
# Libraries
#============================================

import inflection
from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go

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

st.set_page_config( page_title= 'Main Page', page_icon='📊', layout='wide')

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

# 6. Plotar Mapa

def group_map( df1 ): 
    
        df_dados = (df1.loc[:,['restaurant_name','average_cost_for_two','currency','cuisines','aggregate_rating','latitude','longitude']]
                    .groupby(['restaurant_name','average_cost_for_two','currency','cuisines','aggregate_rating']).median().reset_index())                                                                                                                                                                                                                         
        mapa = folium.Map()

        grafico_agrupado = MarkerCluster().add_to( mapa )

        for index, location_info in df_dados.iterrows():
            folium.Marker( [ location_info['latitude'], location_info['longitude'] ],
                           popup=location_info[ ['restaurant_name','average_cost_for_two','currency','cuisines','aggregate_rating'] ],
                           icon=folium.Icon(color='darkred', icon_color='white', icon='home', angle=0, prefix='fa'),).add_to( grafico_agrupado )
        
        folium_static( mapa, width=1024 , height=600)   
        
        return None
    
#----------------------------------------------------- Inicio da Estrutura Lógica do Código ---------------------------------------------


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

#image_path = r'C:\Users\israelguastalle-sao\repos_cds\FTC\projeto_final\streamilit\icone.png'
#image = Image.open( image_path )
#st.sidebar.image( image, width=40)

#============================================
# Para Cloud
#============================================

#image = Image.open( 'icone.png' )
#st.sidebar.image( image, width=120)

#============================================

#----- Criando barra lateral de filtros -----

#st.sidebar.markdown('# Fome Zero!')
#st.sidebar.markdown("""---""")


#============================================
# FILTROS
#============================================

st.sidebar.markdown('## Filtros:')
st.sidebar.markdown('Escolha os Países que deseja visualizar os restaurantes no mapa:')


#----- Criando filro de Países -----

filtro_paises = st.sidebar.multiselect('Quais Países?',
                                        df1.loc[:, 'country'].unique().tolist(),
                                        default = ['Brazil','England','Qatar','South Africa','Canada','Australia'])



#-----Ativando o filtro de Países -----


linhas_selecionadas = df1['country'].isin( filtro_paises )
df1 = df1.loc[linhas_selecionadas, :]


#-------------------------------------


st.sidebar.markdown("""---""")
st.sidebar.markdown('Powered by Israel Guastalle')


#============================================
# LAYOUT NO STREAMLIT
#============================================

st.write('# 📈 Fome Zero!')

#---------Primeira Linha-----------

with st.container():

    st.markdown('### Principais Indicadores:')
    
    col1, col2, col3, col4, col5 = st.columns(5, gap='large')
    
    with col1:
        restaurantes_cadastrados = df2['restaurant_id'].nunique()
        col1.metric('Restaurantes Cadastrados', restaurantes_cadastrados)
        
    with col2:
        paises_cadastrados = df2['country_code'].nunique()
        col2.metric('Países Cadastrados', paises_cadastrados)
        
    with col3:
        cidades_cadastradas = df2['city'].nunique()
        col3.metric('Cidades Cadastradas', cidades_cadastradas)
        
    with col4:
        avaliacoes = df2['votes'].sum()
        votes = (f'{avaliacoes:,f}').replace(",",".")[:9]
        col4.metric('Avaliações Feitas na Plataforma', value=votes)
        
    with col5:
        culinarias_oferecidas = df2['cuisines'].nunique()
        col5.metric('Tipos de Culinárias Oferecidas', culinarias_oferecidas)

    
#---------Segunda Linha------------
        
with st.container():

    #st.title('Location of Restaurants')
    st.markdown('### Localização dos Restaurantes:')
    group_map( df1 )
     
