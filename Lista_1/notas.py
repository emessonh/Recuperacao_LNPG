valor = float(input("Digite o valor: "))
cedulas = [100, 50, 10, 5, 1]
qtd_cedulas = [0, 0, 0, 0, 0]
c = 0
while (c <= 4):
    if (cedulas[c] <= valor):
        while cedulas[c] <= valor:
            qtd_cedulas[c] += 1
            valor = valor - cedulas[c]
    c += 1

i = 0
while (i <= 4):
    if (qtd_cedulas[i] != 0):
        print(f"{qtd_cedulas[i]} nota(s) de {cedulas[i]}") 
    i += 1