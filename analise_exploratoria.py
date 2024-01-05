import pandas as pd 
import matplotlib.pyplot as plt 


df = pd.read_excel('C:\\Users\\lucas.cargnin\\Documents\\Pandas\\AdventureWorks\\AdventureWorks2.xlsx')

df = df.rename(columns= {'OrderDateKey':'Data Pedido', 'ShipDateKey':'Data Envio', 'Order Quantity':'Qtd Pedido', 'Unit Price': 'Preco Unit', 'Product Standard Cost':'Custo Padrao', 'Sales Amount':'Venda R$', 'Total Product Cost':'Custo total'})

df['Lucro'] = df['Venda R$'] - df['Custo total']

# total
total = round(df['Lucro'].sum(),2)

# tempo de envio
df['Tempo envio'] = df['Data Envio'] - df['Data Pedido']

pd.options.display.float_format = '{:20, .2f}'.format

print(df.dtypes)
# tempo envio por local
envio_por_local = df.groupby('SalesTerritoryKey')['Tempo envio'].mean()

# print(df.head())
# print(envio_por_local)

# verificando se tem nulos
# print(df.isnull().sum())

# agrupando por revendedor e ano
# teste = df.groupby([df['Data Pedido'].dt.year,'ResellerKey'])['Lucro'].sum()
# print(teste)

# grafico total produtos vendidos
df.groupby('ResellerKey')['Qtd Pedido'].sum().sort_values(ascending= True).plot.barh(title = 'Produtos por Revendedor')
plt.show()
