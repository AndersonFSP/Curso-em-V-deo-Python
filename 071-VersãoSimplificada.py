print('=' * 30)
print('{:^30}'.format('BANCO DEV'))
print('=' * 30)
valor = int(input('Que valor vc quer sacar ? '))
total = valor
céd = 50
totced = 0
while True:
    if total >= céd:
        total -= céd
        totced +=1
    else:
        if totced > 0:
            print(f'Tota de {totced} cédulas de {céd} reais ')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd ==10:
            céd =5
        elif céd == 5:
            céd = 1
        totced = 0
        if total == 0:
            break
print('Retire seu dinheiro')

