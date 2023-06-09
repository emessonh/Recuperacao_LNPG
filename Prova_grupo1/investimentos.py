cidade = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
passos = input("Digite os passos: ").split()
c = 0
ponto_atual = [0, 0]
while c < 20:
    if passos[c] == "b":
        ponto_atual = [ponto_atual[0]+1, ponto_atual[1]]
        cidade[ponto_atual[0]][ponto_atual[1]] += 1
    elif passos[c] == "c":
        ponto_atual = [ponto_atual[0]-1, ponto_atual[1]]
        cidade[ponto_atual[0]][ponto_atual[1]] += 1
    elif passos[c] == "e":
        ponto_atual = [ponto_atual[0], ponto_atual[1]+1]
        cidade[ponto_atual[0]][ponto_atual[1]] += 1
    elif passos[c] == "d":
        ponto_atual = [ponto_atual[0], ponto_atual[1]-1]
        cidade[ponto_atual[0]][ponto_atual[1]] += 1

    c+=1

maior = cidade[0][0]
for i in cidade:
  for z in i:
    if z > maior:
      maior = z

x = 0
while x < 4:
  y = 0
  while y < 4:
    if cidade[x][y] == maior:
      print(f"Coordenada: X:{y}, Y:{x}")
    y+=1 
  x+=1