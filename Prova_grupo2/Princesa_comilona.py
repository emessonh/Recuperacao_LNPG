comidas_quilos = input("Digite a quantidade de comidas e quilos: ").split()
c = 0
comilanca = []
quilos_comilanca = 0
felicidade_maxima = 0
while c < int(comidas_quilos[0]):
    felicidade_quilos = input("Digite a felicidade e quilos: ").split()
    comilanca.append(felicidade_quilos)
    c+=1

z = 0
while z < len(comilanca):
    if int(comilanca[z][1]) < 0:
        felicidade_maxima += int(comilanca[z][0])
        quilos_comilanca += int(comilanca[z][1])
    z += 1

for i in comilanca:
    if int(i[1]) + quilos_comilanca <= int(comidas_quilos[1]) and int(i[1]) >= 0:
        felicidade_maxima += int(i[0])
        quilos_comilanca += int(i[1])

if felicidade_maxima < 0:
    print("0")
else:
    print(felicidade_maxima)

