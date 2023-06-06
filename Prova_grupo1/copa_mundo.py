def vencedor(placar, jogo):
    if (int(placar[0]) > int(placar[1])):
        return jogo[0]
    else:
        return jogo[1]

jogos = [["A", "B"], ["C", "D"], ["E", "F"], ["G", "H"], ["I", "J"], ["K", "L"], ["M", "N"], ["O", "P"]]
placares = []

c = 0
while c < 15:
    placar = input("Digite o placar: ").split()
    placares.append(placar)
    c += 1

i = 0
while i < 15: 
    if i%2 == 0:  
        jogo = []
        time1 = vencedor(placares[i], jogos[i])
        jogo.append(time1)
        if i == 14:
            print(time1)
    else:
        time2 = vencedor(placares[i], jogos[i])
        jogo.append(time2)
        jogos.append(jogo)
    i += 1
    




