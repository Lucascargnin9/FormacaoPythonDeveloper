import datetime
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pymongo:pymongo@cluster1.yoczfda.mongodb.net/?retryWrites=true&w=majority")

# criando bd
db = client['banco']

# criando colecao para armazenar docs
bank_collection = db['bank']

# criando docs para os clientes e contas
lucas_doc = {
    "nome": "Lucas C",
    "cpf": "123456789",
    "endereco": "Rua Sao Paulo",
    "conta": {
        "tipo": "Conta Salario",
        "agencia": "2699",
        "numero": 12345
    }
}

joao_doc = {
    "nome": "Joao A",
    "cpf": "789654321",
    "endereco": "Rua Rio Janeiro",
    "conta": {
        "tipo": "Conta Corrente",
        "agencia": "6288",
        "numero": 54321
    }
}

# inserindo docs na colecao
bank_collection.insert_one(lucas_doc)
bank_collection.insert_one(joao_doc)

for document in bank_collection.find():
    print(document)

