from database import conexao as db
from controller import functions as fc
from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
import configparser

app = Flask(__name__)
api = Api(app)
#config = configparser.ConfigParser()
# config.read('config.ini')
# db = db.conexao(config['DATABASE']['host'],
#                config['DATABASE']['db'],
#                config['DATABASE']['username'],
#                config['DATABASE']['password'])
#con = db.conectadb()
fc = fc.funcoes()

# Endpoint que gera os vetores isolados dos textos enviados na API
@app.route('/geraVetoresIsolados', methods=["POST"])
def gera_vetores_isolados():
    array = []
    textos = request.json.get('textos')
    for reg in textos:
        array.append(fc.montaVetor(reg))
    return jsonify(array)

# Endpoint que gera o vocabulário de um conjunto de textos
@app.route("/geraVocabularioIsolado", methods=["POST"])
def gera_vocabulario_isolado():
    array = []
    textos = request.json.get('textos')
    for reg in textos:
        array.extend(fc.montaVetor(reg))
    voc = fc.RemoveDuplicados(array)
    return jsonify(fc.removeStopwords(voc))

# Endpoint que gera os vetores (2-gram) dos textos enviados na API
@app.route('/geraVetoresDuplos', methods=["POST"])
def gera_vetores_duplos():
    array = []
    textos = request.json.get('textos')
    for reg in textos:
        array.append(fc.montaVetorDuplo(reg))
    return jsonify(array)

# Endpoint que gera o vocabulário(2-gram) de um conjunto de textos
@app.route("/geraVocabularioDuplo", methods=["POST"])
def gera_vocabulario_duplo():
    array = []
    textos = request.json.get('textos')
    for reg in textos:
        array.extend(fc.montaVetorDuplo(reg))
    voc = fc.RemoveDuplicados(array)
    return jsonify(voc)


if __name__ == '__main__':

    app.run(debug=True)
