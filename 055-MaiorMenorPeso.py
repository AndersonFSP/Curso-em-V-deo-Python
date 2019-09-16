G = 0
P = 0
for c in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(c)))
    if peso > G:
        G = peso
    else:
        P = peso
print('Maior peso: {}Kg\nMenor peso: {}Kg'.format(G, P))


