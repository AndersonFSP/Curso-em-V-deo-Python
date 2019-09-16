from random import randint
from time import sleep
print('-=-' * 20 )
print('Vou pensar em um numeoro de 0 a 5, tente adivinhar... Humano...')
print('-=-' * 20 )
escolhido = randint(0, 5)
chute = int(input('Em que numero pensei ? '))
print('PROCESSAND0 0101001.01111 !')
sleep(1.5)
if escolhido == chute:
    print('Você me ganhou humano pensei {} e você respondeu {}, apenas sorte...'.format(escolhido, chute))
else:
    print('Você errou 0100100100100101, o numero que eu pensei era {} entenda a inferioridade do mundo perante a minha capacidade.'.format(escolhido))