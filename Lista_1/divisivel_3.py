n = int(input("Digite um número: "))
divisao = n%3
if (divisao == 0):
    print(f"{n} é divisível por 3")
else:
    print(f"{n} não é divisível por 3")