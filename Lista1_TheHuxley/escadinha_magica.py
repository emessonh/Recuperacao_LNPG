n = int(input("Digite o número de iteracoes: "))
if n >=1 and n <= 40:
    for i in range(1, n+1):
        for c in range(1, i+1):
            print(c, end=" ")
        print()
else:
    print()