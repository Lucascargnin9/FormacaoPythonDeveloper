from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Lucas', idade=27)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoas = Pessoas.query.all()  # Corrected: Added parentheses to call the function
    for pessoa in pessoas:
        print(f'Nome: {pessoa.nome}, Idade: {pessoa.idade}')

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lucas').first()  # Corrected: Added .first() to get the first result
    if pessoa:
        pessoa.idade = 21
        pessoa.save()
    else:
        print('Pessoa não encontrada.')

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lucas').first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    altera_pessoa()
    consulta()
    exclui_pessoa()
