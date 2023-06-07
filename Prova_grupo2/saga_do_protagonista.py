#possibildiades_de_sub_arrays = tamanho_do_array_A - (tamanho_do_array_B - 1)

def geraPossibilidades(arrayA, lenArrayB, arrayPossibilidades):
    '''Gera todos os subarrays possiveis, dado um determinado array.'''

    if len(arrayA) == lenArrayB:
        arrayPossibilidades.append(arrayA)
    else:
        arrayPossibilidades.append(arrayA[0:lenArrayB])
        return geraPossibilidades(arrayA[1:], lenArrayB, arrayPossibilidades)

def getDigitosMinimosSemelhates(arrayB, arrayPossibilidades):
    '''Retorna a maior quantidade de digitos semelhantes encontrados entre um dado array e subarrays.'''
    qtd_digitos_semelhantes = int()

    for possibilidade in arrayPossibilidades:
        if len(set(arrayB).intersection(possibilidade)) >= qtd_digitos_semelhantes:
            qtd_digitos_semelhantes = len(set(arrayB).intersection(possibilidade))
    
    return qtd_digitos_semelhantes
    
def getArraysMaisSemelhantes(arrayB, arrayPossibilidades):
    '''Retorna os subarrays mais semelhates em relação a um dado array.'''
    qtd_minima_digitos_semelhantes = getDigitosMinimosSemelhates(arrayB, arrayPossibilidades)
    possibilidades_semelhantes = list()

    for possibilidade in arrayPossibilidades:
        if len(set(arrayB).intersection(possibilidade)) >= qtd_minima_digitos_semelhantes:
            possibilidades_semelhantes.append(possibilidade)
    
    return possibilidades_semelhantes

def getSubarrayMaisSemelhante(arrayB, arrayPossibilidades):
    '''Dado um array e uma lista de subarrays, diz qual subarray é o mais semelhante ao array.'''
    pontuacao = int()
    arrayMaisSemelhante = list()

    arraysSemelhantes = getArraysMaisSemelhantes(arrayB, arrayPossibilidades)

    for array in arraysSemelhantes:
        pontuacao_array = int()

        for index_elemento in range(len(arrayB)-1):
            if arrayB[index_elemento] == array[index_elemento]:
                pontuacao_array += 1

        if pontuacao_array >= pontuacao:
            pontuacao = pontuacao_array
            arrayMaisSemelhante = array[:]
        
    return arrayMaisSemelhante

def getQtdModificacoes(arrayB, subarrayMaisSemelhante):
    '''Retorna a quantidade de modificacoes necessarias para um array se igualar a outro.'''
    modificacoes = int()

    for indice, elemento in enumerate(arrayB):
        if arrayB[indice] != subarrayMaisSemelhante[indice]:
            modificacoes += 1
    
    return modificacoes

N = int(input())
A = input().split()

M = int(input())
B = input().split()

subarraysPossiveis = list()
geraPossibilidades(A, len(B), subarraysPossiveis)

subarrayMaisSemelhanteAoB = getSubarrayMaisSemelhante(B, subarraysPossiveis)
numeroDeModificacoes = getQtdModificacoes(B, subarrayMaisSemelhanteAoB)

print(' '.join(str(elemento) for elemento in subarrayMaisSemelhanteAoB))
print(numeroDeModificacoes)
