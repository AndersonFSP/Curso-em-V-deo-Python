from random import randint
c = 0
print('=-'*30)
print('VAMOS JOGAR OU ÍMAPAR')
print('=-'*30)
while True:
    valor = int(input('Digite um valor: '))
    aposta = str(input('Par ou Impar ? [P/I]: ')).upper().strip()
    compValor = randint(0, 10)
    if (valor + compValor) % 2 == 0:
        res = 'PAR'
    else:
        res = 'IMPAR'
    print(f'Você jogou {valor} e o computador {compValor}, o resultado foi {res}')
    print('-'*40)
    if res[0] == aposta[0]:
        print('VOCÊ VENCEU!\nVAMOS JOGAR NOVAMENTE!')
        print('-'*40)
        c += 1
    else:
        break
print(f'GAME OVER!\nvocê venceu {c} vezes')
