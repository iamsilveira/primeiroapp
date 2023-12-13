import streamlit as st 

st.title('Meu Primeiro Aplicativo Streamlit 💙')
st.header('Meu Primeiro Aplicativo Streamlit')
st.write('Meu Primeiro Aplicativo Streamlit')


botao = st.button('Clica em mim')

#input do front-end
numero = st.slider('Escolha um número')

#back-end
frase = f'O número selecionado é {numero} e seu quadrado é {numero**2}'

#resposta de volta ao front-end
st.write(frase)


st.markdown('---')

st.header('💫 A mágica do Streamlit')


n = st.number_input(
	label = 'Entre com um número',
	min_value = 100,
	max_value = 2000,
	step = 100,
	value = 100,
	help = 'Instrução para o widget')

titulo = st.text_input(
	label = 'Entre com o título',
	max_chars = 100,
	placeholder = 'Texto cinzinha')



cor = st.color_picker('Escolha a cor do gráfico')

import numpy as np 
import matplotlib.pyplot as plt

seq = np.random.normal(size = n)

plt.hist(seq, color = cor, edgecolor = 'white')
plt.title(titulo)

st.write(cor)
st.pyplot(plt)


st.markdown('---')

import pandas as pd
link = 'https://raw.githubusercontent.com/ricardorocha86/Datasets/master/Titanic/train.csv'
dados = pd.read_csv(link)

#st.write(dados)

s = st.checkbox('Assinale se quiser apenas sobreviventes')

n1, n2 = st.slider('Idades para filtrar', 
	min_value = 20, 
	max_value = 80,
	value = [40, 60])

filtro1 = dados['Age'] >= n1
filtro2 = dados['Age'] <= n2
filtro3 = dados['Survived'] == 1

if s:
	st.write(dados.loc[filtro1 & filtro2 & filtro3, :])
else:
	st.write(dados.loc[filtro1 & filtro2, :])
