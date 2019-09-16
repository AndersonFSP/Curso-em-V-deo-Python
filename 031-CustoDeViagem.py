distancia = int(input('Qual a distancia da viagem ? '))
print('Você esta prester a percorrer {:.1f}km'.format(distancia))
if distancia < 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua viagem vai ser R${:.2f}'.format(preco))