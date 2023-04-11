# Exemplo 01 - Criar um visualizador de arquivos com 30 linhas

import streamlit as st
import pandas as pd

st.markdown(
'''
# Exibidor de arquivos

## Suba um arquivo e vejamos o que acontece:
'''
)

arquivo = st.file_uploader (
    'Suba seu arquivo aqui',
    type=['jpg','png','csv','py','xlsx','json']
          )

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'image', _:
            st.image(arquivo)
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
        case 'text', 'csv':
            df = pd.read_csv(arquivo)
            st.dataframe(df)
else: st.error("Ainda não tenho arquivo")
            
