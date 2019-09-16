preco = float(input('Qual o preço do seu produto ?'))
desc = preco - (preco * 5 ) / 100
print('o produto que custava R${:.2f},com o desconto de 5% vai custar {:.2f}'.format(preco, desc))
