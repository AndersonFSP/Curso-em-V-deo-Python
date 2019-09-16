real = float(input('Digite o valor em R$ a ser convertido: '))
dolar = real / 3.76
print('Com R${:.2f} você pode comprar US${:.2f} '.format(real, dolar))
