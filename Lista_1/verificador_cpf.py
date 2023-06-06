cpf = input("Digite o seu cpf: ")
c = 0
soma = 0
mult = 10
cont = True
while (c < 9):
    soma += (int(cpf[c]) * mult)
    mult -= 1
    c += 1


resto_divisao = soma % 11
if resto_divisao < 2:
    if (int(cpf[9]) == 0):
        pass
    else:
        print("Cpf inválido")
        cont = False
else:
    subtracao = 11 - resto_divisao
    if (int(cpf[9]) == subtracao):
        pass
    else:
        print("Cpf inválido")
        cont = False

if (cont == True):
    i = 0
    soma2 = 0
    mult2 = 11
    while (i < 10):
        soma2 += (int(cpf[i]) * mult2)
        mult2 -= 1
        i += 1
    
    resto_divisao2 = soma2%11
    if resto_divisao2 < 2:
        if (int(cpf[10]) == 0):
            print("CPF válido")
        else:
            print("Cpf inválido")
            
    else:
        subtracao2 = 11 - resto_divisao2
        if (int(cpf[10]) == subtracao2):
            print("Cpf válido")
        else:
            print("Cpf inválido")
            
