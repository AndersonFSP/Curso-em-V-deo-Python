from random import randint
from time import sleep
c = 0
print('-=-' * 20 )
print('Vou pensar em um numeoro de 0 a 10, tente adivinhar... Humano...')
print('-=-' * 20 )
escolhido = randint(0, 10)
chute = int(input('Em que numero pensei ? '))
while escolhido != chute:
    c += 1
    if chute > escolhido:
        print('Menos... Again')
    else:
        print('Mais... Again')
    chute = int(input('Em que numero pensei ? '))
print('\nAcertou com {} tentativas, parabens'.format(c))



