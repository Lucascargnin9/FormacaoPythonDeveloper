from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {
        'id': '0',
        'nome': 'Lucas',
        'habilidades': ['Python', 'Flask']},
    {
        'id': 1,
        'nome': 'Rafael',
        'habilidades': ['Python', 'Django']}
]

# devolve um dev pelo ID, tambem altera e deleta um dev
@app.route('/dev<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'desenvolvedor de ID {} nao existe'.format(id)
            response = {'status': 'erro', 'mensagem' :mensagem}
        except Exception:
            mensagem = 'erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem' :mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'registro excluido'})

#lista todos os devs e permite registrar um novo
@app.route('/dev/', methods=['POST', 'GET'])
def lista_dev():
    if request.method == 'POST':
        dados = json.loads(request.data)
        devs.append(dados)
        return jsonify({'status': 'sucesso'})
    elif request.method == 'GET':
        return jsonify(devs)


if __name__ == '__main__':
    app.run(debug=True)
