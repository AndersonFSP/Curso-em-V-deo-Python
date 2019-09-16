n = int(input('Digite um numeor para calcular seu fatorial: '))
print('Calculando {}! = '.format(n), end='')
acc = n
while n > 1:
    print('{} x '.format(n), end='')
    acc = acc * (n - 1)
    n -= 1
print('1 = ', acc)
