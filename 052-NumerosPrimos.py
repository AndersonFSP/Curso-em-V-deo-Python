cont = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1 ):
    if num % c == 0:
        print('\33[33m', end='')
        cont += 1
    else:
        print('\33[31m', end='')
    print(c, end=' ')
print("\n\33[mO numero {} foi divisivel {} vezes".format(num, cont))
if cont == 2:
    print('O número é PRIMO')
else:
    print('O numero não é PRIMO')

