tam_bairro = input("Digite N e M: ").split()
bairro = []
c = 0
while (c < int(tam_bairro[0])):
    linha = input("Digite os preços: ").split()
    bairro.append(linha)
    c += 1

precos_avenida = []

i = 0
while (i < int(tam_bairro[1])):
    avenida = []
    for x in bairro:
        avenida.append(x[i])
    precos_avenida.append(avenida)
    i += 1

valores = []
for y in precos_avenida:
    soma = 0
    for s in y:
        soma += int(s)
    valores.append(soma)


menor_valor = valores[0]

for b in valores:
    if (b < menor_valor):
        menor_valor = b

print(menor_valor)





