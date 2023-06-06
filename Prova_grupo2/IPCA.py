dados = []
while True:
    ipca_data = input("Digite o ano e o ipca: ").split(" ")
    if ipca_data[0] == "*":
        break

    ipca = ipca_data[1].split(",")
    ipca = ipca[0] + "." + ipca[1]
    ipca_atual = [ipca_data[0], ipca]

    dados.append(ipca_atual)

menor = float(dados[0][1])
data_menor = dados[0][0]
maior = float(dados[0][1])
data_maior = dados[0][0]
media = 0

for i in dados:
    # menor IPCA
    if float(i[1]) < menor:
        menor = float(i[1])
        data_menor = i[0]
    #maior IPCA
    if float(i[1]) > maior:
        maior = float(i[1])
        data_maior = i[0]

    media += float(i[1])

media = media/len(dados)
data_menor = data_menor.split("-")
data_maior = data_maior.split("-")
data_menor = data_menor[1]+"-"+data_menor[0]
data_maior = data_maior[1]+"-"+data_maior[0]

print(f"Menor: {menor} ({data_menor})")
print(f"Maior: {maior} ({data_maior})")
print(f"Media: {media:.2f}")