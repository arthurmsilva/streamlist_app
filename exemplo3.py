########## Exemplo 03 - Aprender a utilizar os layouts ###########

import streamlit as st
from spacy import load, displacy
from streamlit.components import v1 as components # gerar renderização html

# Carregando as informações da análise de texto
nlp = load('pt_core_news_lg')

# Criando um sidebar (Barra lateral)
bar = st.sidebar

# Criando uma barra de escolha a ser colocada no sidebar
escolha = bar.selectbox(
    'Escolha uma categoria',
    ['Entidades', 'Gramática']
)

# Criando uma barra de texto longo
text = st.text_area('Escreva um texto longo:')

# Realizando a análise do texto
doc = nlp(text)

# Se escolha Entidade, dividir em duas colunas apresentando as entidades e o tipo das mesmas
if text and escolha == 'Entidades':
    data = displacy.render(doc, style='ent') # spacy gera um html
    
    with st.expander('Dados do spacy'):
        components.html(
            data,
            scrolling=True,
            height=300
        )
    a, b = st.columns(2)
    for e in doc.ents:
        a.info(e)
        b.warning(e.label_)

# Se escolha Gramática, aparece um filtro adicional onde o usuário seleciona o tipo gramático
## Verbo, pronome, adverbio, etc
if text and escolha == 'Gramática':
    filtro = bar.multiselect(
        'Filtro',
        ['VERB', 'PROPN', 'ADV', 'AUX'],
        default=['VERB', 'PROPN']
        )
    # Apresentando os dados json
    with st.expander('Dados do spacy'):
        st.json(doc.to_json())
    
    # Criação de containers para apresentar mais de uma info ao mesmo tempo
    container = st.container()
    
    a,b,c = container.columns(3) # Definindo as três colunas

    a.subheader('Token')
    b.subheader('Tag')
    c.subheader('Morph')
    
    # Loop para criar a estrutura para cada palavra 
    for t in doc:
        if t.tag_ in filtro:
            container = st.container() # Novo container somente para organizar os dados
            a,b,c = container.columns(3)
            
            a.info(t)
            b.warning(t.tag_)
            c.error(t.morph)
