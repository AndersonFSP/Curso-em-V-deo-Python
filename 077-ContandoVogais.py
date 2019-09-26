palavras = ('aprender', 'programar', 'python', 'cobra', 'anderson')
str= ''
# for c in range(len(palavras)):
#     print(f'Na palavra {palavras[c].upper()} temos: ', end='')
#     for i in range(len(palavras[c])):
#         str = palavras[c]
#         if str[i].upper() in 'AEIOU':
#             print(str[i], end=' ')
#     print()

for p in palavras:
    print(f'\nNa palvra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

