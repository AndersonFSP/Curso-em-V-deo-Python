soma = 0
for c in range(0+1 , 6):
    num = int(input('Digite o {} valor : '.format(c)))
    if num % 2 == 0:
        soma += num
print('Soma de numeros pares: {}'.format(soma))
