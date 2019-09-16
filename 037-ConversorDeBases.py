n = int(input('Digite um Número Inteiro: '))
print('Escolha uma das Bases de conversão: ')
print('[ 1 ] converter para Binário \n[ 2 ] converter para Octal \n[ 3 ] converter para Hexadecimal')
opt = int(input('Sua opção de 1 a 3: '))

if opt == 1 :
    print('{} convertido para Binário é igual a {}'.format(n, bin(n)))
elif opt == 2 :
    print('{} convertido para Octal é igual a {}'.format(n, oct(n)))
elif opt == 3 :
    print('{} convertido para Octal é igual a {}'.format(n, hex(n)))
else:
    print('Entrada inválida ')
