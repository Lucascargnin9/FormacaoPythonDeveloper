from flask import Flask, jsonify
import json

app = Flask(__name__)

# Carrega os dados do arquivo JSON
with open('dados.json', 'r') as file:
    dados = json.load(file)

@app.route('/planilha', methods=['GET'])
def obter_planilha():
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)


