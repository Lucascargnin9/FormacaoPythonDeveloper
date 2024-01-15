from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

devs = [
    {
        'id': 0,
        'nome': 'Lucas',
        'habilidades': ['Python', 'Flask']},
    {
        'id': 1,
        'nome': 'Rafael',
        'habilidades': ['Python', 'Django']}
]

class Dev(Resource):

    def get(self,id):
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'desenvolvedor de ID {} nao existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}

        return response

    def put(self):

        dados = json.loads(request.data)
        devs[id]=dados
        return dados

    def delete(self):
        devs.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluido'}

#lista todos os devs e permite registrar um novo
class ListaDevs(Resource):

    def get(self):
        return devs

    def post(self):
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)

        return devs[posicao]


api.add_resource(Dev, '/dev/<int:id>/')
api.add_resource(ListaDevs, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run()