qtd_blocos = int(input("Digite a qtd de blocos: "))
torres = []
if (qtd_blocos >= 1 and qtd_blocos <= 1000):
    tamanho_blocos = input("Digite os tamanhos dos blocos: ").split()
    elementos_excluidos = []
    for i in tamanho_blocos:
        if (len(elementos_excluidos) == 0):
                tamanho_torre = tamanho_blocos.count(i)
                elementos_excluidos.append(i)
                torres.append(tamanho_torre)
        else:
            if (i not in elementos_excluidos):
                tamanho_torre = tamanho_blocos.count(i)
                elementos_excluidos.append(i)
                torres.append(tamanho_torre)
        
else:
    print("Número muito grande!")

maior_torre = torres[0]

for x in torres:
    if x > maior_torre:
        maior_torre = x 

print(f"{maior_torre} {len(torres)}")