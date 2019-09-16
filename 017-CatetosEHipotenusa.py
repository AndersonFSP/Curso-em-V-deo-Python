import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa deve medir {:.2f}'.format(math.hypot(ca, co)))

