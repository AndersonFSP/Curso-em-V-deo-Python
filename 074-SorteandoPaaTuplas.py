from random import randint
maior = menor = 0
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for c in range(len(numeros)):
    print(numeros[c], end=' ')    #PARA QUESTÃO MAIOR E MENOR POSSO USAR O  max(numeros) e min(numeros)
    if c == 0:
        maior = numeros[c]
        menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print('')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')




