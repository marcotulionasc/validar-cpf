class ValidadorCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def validar_cpf(self):
        cpf = self.cpf.replace(".", "").replace("-", "")

        if len(cpf) != 11 or not cpf.isdigit():
            return False

        # Verificar se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False

        # Verificar os dígitos verificadores
        digitos = cpf[:-2]
        dv1 = self.calcular_digito_verificador(digitos)
        dv2 = self.calcular_digito_verificador(digitos + str(dv1))

        return cpf[-2:] == str(dv1) + str(dv2)

    @staticmethod
    def calcular_digito_verificador(digitos):
        soma = 0
        peso = 10

        for digito in digitos:
            soma += int(digito) * peso
            peso -= 1

        resto = soma % 11
        if resto < 2:
            return 0
        else:
            return 11 - resto


# Vamos fazer um teste!
cpf = input("Digite um CPF: ")
validador = ValidadorCPF(cpf)
if validador.validar_cpf():
    print("CPF válido!")
else:
    print("CPF inválido!")
