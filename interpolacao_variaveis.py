nome="teste"
idade=26
profissao="teste"
linguagem="Python"
saldo=45.425


dados = {"nome":"Teste","idade":28}

print("nome: %s idade: %d" % (nome,idade))
print("nome: {} idade: {}". format(nome,idade))
print("nome: {0} idade: {1}".format(nome,idade))
print("nome: {nome} idade: {idade}".format(nome=nome,idade=idade))

print("nome: {nome} idade: {idade}".format(**dados))

print(f"nome: {nome} idade: {idade}")

print(f"nome: {nome} idade: {idade} saldo:{saldo: .2f}")