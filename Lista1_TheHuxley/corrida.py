competicao = input("Digite o número de competidores e voltas: ").split()
tempos = []
c = 0
while c < int(competicao[0]):
    soma_tempos = 0
    tempo_comp = input("Digite os tempos: ").split()
    i = 0
    while i < int(competicao[1]):
        soma_tempos += int(tempo_comp[i])
        i += 1
    tempos.append(soma_tempos)

    c += 1

menor_tempo = tempos[0]
x = 0
competidor_venc = 1
while x < len(tempos):
    if (tempos[x] < menor_tempo):
        menor_tempo = tempos[x]
        competidor_venc = x + 1
    x += 1

print(competidor_venc)