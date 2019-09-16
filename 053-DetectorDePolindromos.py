frase = input('Digite a Frase: ').upper().strip().replace(' ', '')
invert = ''
tam = len(frase)
for c in range(tam - 1, -1, -1):
    invert += frase[c]
print('O inverso de \33[33m{}\33[m é \33[31m{}\33[m'.format(frase, invert))
if frase == invert:
    print('A frase é um pálindromo')
else:
    print('Não é um pálindromo')
