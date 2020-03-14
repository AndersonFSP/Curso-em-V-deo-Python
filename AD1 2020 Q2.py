def resposta(primos):
    print('Relação de Primos(s):')
    for j in range(len(primos)):
        print(primos[j])
    print('Fim da Relação.')


def separaNumerosPrimos(numeros):
    for c in range(len(numeros)):
        cont = 0
        for i in range(1, numeros[c]+1):
            if numeros[c] % i == 0:
                cont += 1
        if cont == 2:
            numerosPrimos.append(numeros[c])
    return numerosPrimos


def verificaLista(numeros):
    if len(numeros) == 0:
        print('Nenhum numero foi lido')
    else:
        primos = separaNumerosPrimos(numeros)
        resposta(primos)


numerosPrimos = []
numeros = list(map(int, input().split()))
verificaLista(numeros)

