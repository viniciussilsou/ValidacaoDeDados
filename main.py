from jsonFile import abrirjson,gravarDadosJson
import validarDados


def main():

    cpf = validarDados.validarcpf()
    dados = {'cpf': cpf}
    listadedados = []
    listadedados.append(dados)
    print(listadedados)
    gravarDadosJson(listadedados)

main()