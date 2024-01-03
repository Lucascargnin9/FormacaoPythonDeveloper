import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']

print('IP: {0} \nPais: {1}\n Cidade: {2}\n Org: {3}'.format(ip, pais, cidade, pais))

