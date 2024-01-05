import pandas as pd 
import matplotlib.pyplot as plt


df1 = pd.read_excel('C:\\Users\\lucas.cargnin\\Documents\\Pandas\\excel\\analia.xlsx')
df2 = pd.read_excel('C:\\Users\\lucas.cargnin\\Documents\\Pandas\\excel\\barigui.xlsx')
df3 = pd.read_excel('C:\\Users\\lucas.cargnin\\Documents\\Pandas\\excel\\mueller.xlsx')
df4 = pd.read_excel('C:\\Users\\lucas.cargnin\\Documents\\Pandas\\excel\\salvador.xlsx')

# print(df1.head())

df = pd.concat([df1, df2, df3, df4])

# print(df.sample(5))
print(df.dtypes)
# print(df['Vendas R$'].mean())

# df['Vendas R$'].fillna(df['Vendas R$'].mean(), inplace= True) #substituindo nulos pela media

maior_venda = df['Vendas R$'].max()
#print(maior_venda)

venda_loja = df.groupby('Loja')['Vendas R$'].sum()
#print(venda_loja)

top10 = df.sort_values('Vendas R$', ascending= False).head(10)
#print(top10)

qtd_venda_loja = df['Loja'].value_counts(ascending= False)
#print(qtd_venda_loja)

# -------------------------------------------------------------
# TRABALHANDO COM DATAS - explicacao

#convertendo data em int
# df['Data'] = df['Data'].astype('int64')
#transformando coluna de data em data
# df['Data'] = pd.to_datetime(df['Data'])
#agrupamento por ano
# df.groupby(df['Data'].dt.year)['Vendas R$'].sum()
#criando nova coluna com o ano
# df['Ano'] = df['Data'].dt.year
#extraindo mes e dia
# df['mes_venda'], df['dia_venda'] = (df['Data'].dt.month, df['Data'].dt.day)

#diferenca entre dias
# df['Diferenca_dias'] = df['Data'] - df['Data'].min()

#criando coluna trimestre
# df['Trimestre'] = df['Data'].dt.quarter

#filtrando vendas de um mes
# venda_mes = df.loc[(df['Data'].dt.year == 2022) & (df['Data'].dt.month == 3)]


#-----------------------------------------------------
# VISUALIZACAO DE DADOS
# plt.show() #comando para plotar os graficos

#barras verticais
# df['Loja'].value_counts(ascending= False).plot.bar()

#barras horizontais
# df['Loja'].value_counts(ascending= False).plot.barh()
#decrescente
# df['Loja'].value_counts(ascending= True).plot.barh()

#grafico de pizza
# df.groupby(df['Data'].dt.year)['Vendas R$'].sum().plot.pie()

#total vendas por loja e colocando legenda no eixo
# df['Loja'].value_counts().plot.bar(title = 'Total vendas por loja')
# plt.xlabel('Loja')
# plt.ylabel('Qtd vendas')
# plt.show()

#alterando cor
# df['Loja'].value_counts().plot(title = 'Total vendas por loja', color='red')
# plt.xlabel('Loja')
# plt.ylabel('Qtd vendas')
# plt.show()

#alterando estilo
# plt.style.use('ggplot')
# plt.show()

#Venda por mes
df.groupby(['Mês'])['Vendas R$'].sum().plot.bar()
plt.show()





