from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebendo o conteudo da requisicao http do site
soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site o html
print(soup.prettify())
#vai exibir o codigo html do site

#temperatura = soup.find('span', class_='_block _margin-b-5 -gray')
#print(temperatura.string)

print(soup.a)
