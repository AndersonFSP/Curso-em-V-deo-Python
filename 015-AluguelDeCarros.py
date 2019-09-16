print('======ALUGEL DE CARROS======')
dias = float(input('Quantidades de dias do aluguel do carro: '))
km = float(input('Km percorridos: '))
valor = (dias * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(valor))

