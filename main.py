from jsonFile import abrirjson,gravarDadosJson
import validarDados


def main():
    cnpj = validarDados.validarCnpj()
    cpf = validarDados.validarcpf()
    dados = {'cpf': cpf, 'cnpj':cnpj}
    listadedados = []
    listadedados.append(dados)
    gravarDadosJson(listadedados)

main()