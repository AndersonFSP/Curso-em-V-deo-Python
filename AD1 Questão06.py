from random import randint
def mostrarMatriz():
    for i in range(a[0]):
        for j in range(a[1]):
            print(valores[i][j], end=" ")
        print()
    print()
def ordemNova():
    for i in range(a[0]):
        soma = 0
        for j in range(a[1]):
            soma += valores[i][j]
            ordemSoma[i] = soma
            ordemNona[i] = i
    for i in range(len(ordemSoma)):
        for j in range(len(ordemSoma)):
            if ordemSoma[i] < ordemSoma[j]:
                aux1 = ordemNona[i]
                aux = ordemSoma[i]
                ordemNona[i] = ordemNona[j]
                ordemSoma[i] = ordemSoma[j]
                ordemNona[j] = aux1
                ordemSoma[j] = aux
    print()

    for i in range(a[0]):
        for j in range(a[1]):
            print(valores[ordemNona[i]][j], end=" ")
        print()
    print()


aux = soma = 0
valores = []
a = list(map(int, input().split()))
valores = [None] * a[0]
ordemSoma = [None] * a[0]
ordemNona = [None] * a[0]
for i in range(a[0]):
    valores[i] = [0] * a[1]
    for j in range(a[1]):
        valores[i][j] = randint(10, 99)

mostrarMatriz()
ordemNova()




