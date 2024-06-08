import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_title="Raciocínio Algorítmico: Aula 07-06",
    page_icon="🤓",
)

st.header("Aula 07/06") 
st.subheader("Adaptação do Código")

"---"

st.write('''**Exercício 1** - Leia o arquivo empresa1.csv e apresente os resultados 3 primeiros resultados da tabela usando o método head()

Exigência: deve utilizar o pacote panda 🐼''')

code = '''
arquivo = "https://raw.githubusercontent.com/paolaribeiroq/criando_stm/main/empresa1.csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe.head(3))
'''
st.code(code, language='python')

arquivo = "https://raw.githubusercontent.com/paolaribeiroq/criando_stm/main/empresa1.csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe.head(3))

"---"

st.write("**Exercício 2** - Apresente os dados do dataframe utilizando gráficos. Crie um gráfico de linha, simples, que apresente todos os indicadores ao longo do tempo. Crie um gráfico de dispersão para ajudar na relação entre EBITDA e Lucro operacional. Crie um histograma do Lucro do período. 📊")

code = '''
fig, ax = plt.subplots()
dfe.plot(ax=ax)
st.pyplot(fig)
'''
st.code(code, language='python')

fig, ax = plt.subplots()
dfe.plot(ax=ax)
st.pyplot(fig)

code = '''
fig, ax = plt.subplots()
dfe.plot(kind = 'scatter', x = 'EBITDA', y = 'Lucro operacional', ax=ax)
st.pyplot(fig)
'''
st.code(code, language='python')

fig, ax = plt.subplots()
dfe.plot(kind = 'scatter', x = 'EBITDA', y = 'Lucro operacional', ax=ax)
st.pyplot(fig)

code = '''
fig, ax = plt.subplots()
dfe["Lucro do período"].plot(kind = 'hist')
st.pyplot(fig)
'''
st.code(code, language='python')

fig, ax = plt.subplots()
dfe["Lucro do período"].plot(kind = 'hist')
st.pyplot(fig)

"---"

st.write("**Exercício 3** - Agrupe a base acima por ano, em um novo dataframe, e apresente a soma das demais coluna 🧾")

code = '''
st.write(dfe.groupby('Ano').mean())
'''
st.code(code, language='python')

st.write(dfe.groupby('Ano').mean())

"---"
