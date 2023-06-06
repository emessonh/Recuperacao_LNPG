dias = int(input("Digite a qtd de dias: "))
c = 0
plano_viagem = []
while c < dias:
    movimento = input("Digite o movimento: ").upper()
    plano_viagem.append(movimento)
    c += 1

x = 0
y = 0
dia1 = []
moedas = 0
terreno = str()
ponto_muralha = False

for i in plano_viagem:
    if i == "D":
        x += 1
        if len(dia1) == 0:
            terreno = "BAIXO"
            dia1.append(x)
            dia1.append(y)
    elif i == "C":
        y += 1
        if len(dia1) == 0:
            terreno = "ALTO"
            dia1.append(x)
            dia1.append(y)

    if ponto_muralha == True and terreno == "ALTO" and y-x < 0:
        moedas += 1 
        terreno = "BAIXO"
    elif ponto_muralha == True and terreno == "BAIXO" and y-x > 0:
        moedas += 1 
        terreno = "ALTO"


    muralha = y-x
    if (muralha == 0):
        ponto_muralha = True
    elif (muralha != 0):
        ponto_muralha = False
   
print(moedas)