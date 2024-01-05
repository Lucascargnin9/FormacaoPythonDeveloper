import pandas as pd 

dataframe = pd.read_csv(r'C:\Users\lucas.cargnin\Documents\Pandas\gapminder\gapminder.csv')

# print(dataframe.head())

dataframe = dataframe.rename(columns= {'country':'Pais', 'continent':'continente', 'lifeExp':'expectativa de vida', 'pop':'populacao', 'gdpPercap':'PIB'})
print(dataframe.head(10))

# print(dataframe.shape)

# print(dataframe.dtypes)

# print(dataframe.describe())

Oceania = dataframe.loc[dataframe['continente'] == 'Oceania']
# print(Oceania)

qtd_pais = dataframe.groupby('continente')['Pais'].nunique()
print(qtd_pais)

expectativa_media = dataframe.groupby('year')['expectativa de vida'].mean() #media
print(expectativa_media)

