n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opt = 0
while opt  < 5:
    print('=-==' * 5)
    print('''[ 1 ]Somar
[ 2 ]Multiplicar
[ 3 ]Maior
[ 4 ]Novos Numeros
[ 5 ]Sair''')
    print('=-==' * 5)
    opt = int(input('>>>Sua opção: '))
    if opt == 1:
        resultado = n1 + n2
        print('A soma de {} e {} é {}'.format(n1, n2, resultado))
    elif opt == 2:
        resultado = n1 * n2
        print('A multiplicação de {} e {} é {}'.format(n1, n2, resultado))
    elif opt == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('{} e {} são iguais '.format(n1, n2))
    elif opt == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    else:
        opt = 5
print('SAINDO ...')


