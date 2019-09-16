from datetime import date
anoAtual = date.today().year
pessoas = 0
for c in range(1, 7):
    anoNasc = int(input('Ano de nascimento da {} pessoa: '.format(c)))
    if anoAtual - anoNasc >= 18:
        pessoas += 1

print('\nAo todo tiveram {} maiores de idade'.format(pessoas))
print('E também {} pessoas menores de idade'.format(6 - pessoas))

