soma = prod1000 = menor = 0
menorNome = ''
print('-' * 30)
print('LOJAS SUPER BARATÃO')
print('-' * 30)
while True:
    nome = str(input('Mome:'))
    preco = float(input('Preco: R$ '))
    if soma == 0:
        menor = preco
        menorNome = nome
    if preco > 1000:
        prod1000 += 1
    if preco < menor:
        menor = preco
        menorNome = nome
    conti = ' '
    soma += preco
    while conti not in 'SN':
        conti = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    if conti == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${soma:.2f}\nTemos {prod1000} produtos que custam mais de R$1000.00\nO produto mais barato foi {menorNome} e custa R${menor:.2f}')


