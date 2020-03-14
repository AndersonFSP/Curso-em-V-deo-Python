from random import randint


def buscaValor(K, lista):
    contador = lista.count(K)
    if contador > 0:
        index = lista.index(K)
    else:
        index = 'Valor não encontrado'
    print(f'K: {K}\nIndice: {index}')


def mostraValores(lista):
    print('Valores:', end=' ')
    for i in range(len(valoresSorteados)):
        print(valoresSorteados[i], end=' ')
    print()

def numeroSorteios(sorteios):
    for c in range(sorteios):
        valoresSorteados.append(randint(0, 10))
    mostraValores(valoresSorteados)
    K = randint(0, 10)
    buscaValor(K, valoresSorteados)


valoresSorteados = []
numeroSorteios(int(input()))
