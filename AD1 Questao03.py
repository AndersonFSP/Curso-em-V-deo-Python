from random import randint
maior = soma = 0
matriz = []
x = 0
y = 0
a = list(map(int, input().strip().split()))
matriz = [None] * a[0]
for i in range(a[0]):
    matriz[i] = [0] * a[1]
    for j in range(a[1]):
        matriz[i][j] = randint(100, 999)


for i in range(a[0]):
    soma += matriz[i][i]
    for j in range(a[1]):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            x = i
            y = j
        print(matriz[i][j], end=" ")
    print()
print()

def somas(linha, coluna):
    for i in range(linha):
        soma = 0
        for j in range(coluna):
            soma += matriz[i][j]
        print('Soma da linha {}= {} '.format(i, soma))

    print()

    for j in range(coluna):
        soma = 0
        for i in range(linha):
            soma += matriz[i][j]
        print('Soma da coluna {}= {} '.format(j, soma))


print('Posição do maior: ({},{}) Maior valor {}'.format(x, y, maior))
print()
somas(a[0], a[1])

