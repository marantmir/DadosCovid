# Importando as bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo o dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Melhorando o nome das colunas da tabela
df = df.rename(columns={'newDeaths' : 'Novos Óbitos', 'newCases' : 'Novos Casos',
                        'deaths_per_100k_inhabitants' : 'Óbitos por 100 mil habitantes',
                        'totalCases_per_100k_inhabitants' : 'Casos por 100 mil habitantes'})



# Gerando lista de estados
estados = list(df['state'].unique( ))

# Seleção do estado
state = st.sidebar.selectbox('Qual o Estado?', estados)

# Seleção da coluna
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual o tipo de informação?', colunas)

# Seleção das linhas que pertencem ao estado
df = df[df['state'] == state]

# Gerando o gráfico
fig = px.line(df, x='date', y=column, title=column + ' - ' + state)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper( ), title={'x' : 0.5})

st.title('DADOS COVID - BRASIL')
st.write(
    'Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu latera para escolher o estado desejado')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
