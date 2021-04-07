

def validarcpf():

    cpf = str(input("Digite CPF:\n"))

    if len(cpf) != 11:
        print("CPF INVALIDO !\nDeve conter até 11 digitos !\n")
        validarcpf()
    elif len(cpf) == 11:
        cpf = ("{}.{}.{}-{}".format(cpf[:3],cpf[3:6],cpf[6:9],cpf[9:]))
        return cpf

def validarCnpj():

    cnpj = str(input("Digite CNPJ:\n"))

    if len(cnpj) != 14:
        print("CNPJ INVALIDO!\n")
        validarCnpj()
    elif len(cnpj) == 14:
        cnpj = ("{}.{}.{}/{}-{}".format(cnpj[:2],cnpj[2:5],cnpj[5:8],cnpj[8:12],cnpj[12:14]))
        return cnpj

def validarEmail():

    email = str(input("Digite E-mail:\n"))

    if '@' in email:
        return email
    else:
        print("E-mail INVÁLIDO !\n")
        validarEmail()

def validarCEP():

    cep = int(input("Digite CEP:\n"))

    if type(cep) == int:
        cep = str(cep)

        if len(cep) != 8:
            print("CEP INVALIDO !\n")
            validarCEP()
        else:
            return cep
    else:
        print("Digite somente Números ! \n")




