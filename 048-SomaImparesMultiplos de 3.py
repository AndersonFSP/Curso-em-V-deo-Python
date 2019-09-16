soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0 and c:
        soma += c
        cont += 1
print('Soma: {} e foram {} numeros'.format(soma, cont))

