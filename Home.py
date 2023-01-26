import streamlit as st
import emoji
from PIL import Image
import pandas as pd

#Função para juntar no streamlit. Ele entende que ele precisa buscar algo em uma pasta pages.

st.set_page_config(
    page_title="Home",
    page_icon="📈"
    #,layout="wide"
)

#image_path = r'C:\Users\israelguastalle-sao\repos_cds\FTC\projeto_final\streamilit\icone.png'
#image = Image.open( image_path )
#st.sidebar.image( image, width=40)

#============================================
# Para Cloud
#============================================

image = Image.open( 'icone.png' )
st.sidebar.image( image, width=120)

#============================================

st.sidebar.markdown( '## Encontre o seu lugar favorito!' )
st.sidebar.markdown( """---""" )

#============================================
# Baixar Dados
#============================================

st.sidebar.markdown( '### Baixe os Dados Tratados:' )

#data=pd.read_csv(r'C:\Users\israelguastalle-sao\repos_cds\FTC\projeto_final\dados.csv')

data = pd.read_csv( 'dataset/dados.csv' )

st.sidebar.download_button(
        label="Download Data",
        data=data.to_csv(index=False, sep=";"),
        file_name="data.csv",
        mime="text/csv")

#============================================

st.sidebar.markdown("""---""")
st.sidebar.markdown('Powered by Israel Guastalle')

#============================================
# Main Page
#============================================

st.write('# 📈 Fome Zero!')

st.markdown( 
    """
     O Melhor lugar para encontrar seu mais novo restaurante favorito!
    ### Como utilizar esse Dashboard?
    
    - Main Page:
         Análise geográfica e Principais Indicadores.
   
    - Countries:
         Acompanhamento dos indicadores pelo panorama de países.
    
    - Cities:
         Acompanhamento dos indicadores pelo panorama de cidades.
        
    - Cuisines:
         Acompanhamento dos indicadores pelo panorama de culinária.
    
    ### Ask for Help:
        - Israel Guastalle  
    
    """)

 
















