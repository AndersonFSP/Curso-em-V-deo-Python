from random import randint
from time import sleep
itens=['pedra', 'papel', 'tesoura']
IA = randint(0,2)
print('''OPÇÔES 
[ 0 ] Pedra 
[ 1 ] Papel
[ 2 ] Tesoura ''')
jog = int(input('Qual é a sua escolha ? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.4)
print('-=' * 13)
print('O computador jogou {}'.format(itens[IA]))
print('O jogador jogou {}'.format(itens[jog]))
print('-=' * 13)

if IA == 0:
    if jog == 0:
        print('EMPATE')
    elif jog ==1:
        print('Jogador VENCE')
    elif jog ==2:
        print('Computador VENCE')
    else:
        print('Jogada INVALIDA')
elif IA == 1:
    if jog == 0:
        print('Computador VENCE')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('Jogador VENCE')
    else:
        print('Jogada INVALIDA')
elif IA == 2:
    if jog == 0:
        print('Jogador VENCE')
    elif jog == 1:
        print('Computador VENCE')
    elif jog == 2:
        print('EMPATE')
    else:
        print('Jogada INVALIDA')





