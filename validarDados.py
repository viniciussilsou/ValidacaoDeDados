
def validarcpf():

    cpf = int(input("Digite CPF:\n"))

    if type(cpf) == int:
        cpf = str(cpf)
        if len(cpf) != 11:
            print("CPF INVALIDO !\nDeve conter até 11 digitos !")
            validarcpf()
        elif len(cpf) == 11:
            cpf = ("{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]))
            return cpf
    else:
        print("Somente Numeros !")

def validarCnpj():

    cnpj = int(input("Digite CNPJ:\n"))

    if type(cnpj) == int:
        cnpj = str(cnpj)
        if len(cnpj) != 14:
            print("CNPJ INVALIDO!")
            validarCnpj()
        elif len(cnpj) == 14:
            cnpj = ("{}.{}.{}/{}-{}".format(cnpj[:2],cnpj[2:5],cnpj[5:8],cnpj[8:12],cnpj[12:14]))
            return cnpj
    else:
        print("Somente Numeros !")

def validarEmail():

    email = str(input("Digite E-mail:\n"))
    if '@' in email:
        return email
    else:
        print("E-mail INVÁLIDO !")
        validarEmail()

def validarCEP():

    cep = int(input("Digite CEP:\n"))

    if type(cep) == int:
        cep = str(cep)
        if len(cep) != 8:
            print("CEP INVALIDO !")
            validarCEP()
        else:
            return cep
    else:
        print("Digite somente Números !")




