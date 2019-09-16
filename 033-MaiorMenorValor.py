a = int(input('Digite o valor: '))
b = int(input('Digite o valor: '))
c = int(input('Digite o valor: '))
menor = a
maior = b
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor digito foi {} e o maior foi {}'.format(menor, maior))