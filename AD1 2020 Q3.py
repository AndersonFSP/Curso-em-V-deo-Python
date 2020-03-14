from random import randint

def exibe(numerosMaioresMedia):
    print('Relação de Valores nas Bordas Acima da Média:')
    for c in range(len(numerosMaioresMedia)):
        print(f'{numerosMaioresMedia[c]}')


def verificaMediaComColunas(matriz, entrada, media):
     linha = coluna =  0
     maioresMedia = []
     for i in range(entrada[0]):
        linha += 1
        if (matriz[coluna][0] > media):
            maioresMedia.append(matriz[coluna][0])
        elif(matriz[coluna][entrada[1]-1] > media):
            maioresMedia.append(matriz[coluna][entrada[1]-1])
        coluna += 1

        for j in range(entrada[1]):
            if (linha == 1 or linha == entrada[0]) and matriz[i][j] > media:
                if j > 0 and j < entrada[0]:
                    maioresMedia.append(matriz[i][j])
     return maioresMedia


def retiraMedia(soma, cont):
    media = soma / cont
    return media

def calculaValores(entrada):
    soma = cont = 0
    for i in range(entrada[0]):
        for j in range(entrada[1]):
            soma += matriz[i][j]
            cont += 1
    media = retiraMedia(soma, cont)
    numerosMaioresMedia = verificaMediaComColunas(matriz, entrada, media)
    print(f'Média dos Valores Sorteados:\n{media:.1f}')
    exibe(numerosMaioresMedia)


def mostraMatriz(entrada):
    for i in range(entrada[0]):
        for j in range(entrada[1]):
            print(f'{matriz[i][j]} ', end=" ")
        print()
    print()
    calculaValores(entrada)


def geraMatriz(entrada):
    for i in range(entrada[0]):
        matriz[i] = [0] * entrada[1]
        for j in range(entrada[1]):
            matriz[i][j] = randint(entrada[2], entrada[3])
    mostraMatriz(entrada)


entrada = list(map(int, input().strip().split()))
matriz = [None] * entrada[0]
print('Conteúdo da Matriz:')
geraMatriz(entrada)



