import json

def abrirjson():

    with open("validacao.json") as arquivo:

        dados = json.load(arquivo)

        return dados

def gravarDadosJson(dados):

    with open("validacao.json","w") as arquivo:

        listadedados = json.dumps(dados, indent=4)
        arquivo.write(listadedados)

