while True:
    n = int(input('Digite um numero para ver a Tabuada: '))
    if n < 0:
        break
    for c in range(0,11):
        print(f'{c} x {n} = {c*n}')
    print('-' * 30)
print('Terminou a operação')