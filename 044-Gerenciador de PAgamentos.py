print('=' * 11, 'LOJAS FILIPE', '=' * 11)
preco = float(input('Preço das compras: R$ '))
print('''Formas de Pagamento 
 [ 1 ] à vista dinheiro/chefe
 [ 2 ] à vista cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão''')
opt = int(input('Qual é a opção ?'))

if opt == 1:
    print('Sua compra de R${} vai custar R${} no final'.format(preco, preco - (preco * 10) / 100))
elif opt == 2:
    print('Sua compra de R${} vai custar R${} no final'.format(preco, preco - (preco * 5) / 100))
elif opt == 3:
    print('Sua compra de R${} vai custar R${} no final'.format(preco, preco))
elif opt ==4:
    parcelas = int(input('Numero de Parcelas: '))
    print('Sua compra parcelada em {:.2f}x de {:.2f} COM JUROS'.format(parcelas, (((preco * 20) / 100) + preco) / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, ((preco * 20)/100) + preco))
else:
    print('Opcao INVALIDA ')