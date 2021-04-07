from jsonFile import abrirjson,gravarDadosJson
import validarDados


def main():
    email = validarDados.validarEmail()
    cnpj = validarDados.validarCnpj()
    cpf = validarDados.validarcpf()
    cep = validarDados.validarCEP()

    dados = {'cpf': cpf, 'cnpj': cnpj, 'e-mail': email, 'cep': cep}

    jsonlist = abrirjson()
    jsonlist.append(dados)

    gravarDadosJson(jsonlist)

main()