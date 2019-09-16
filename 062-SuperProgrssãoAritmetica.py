print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
inicio = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
c = 0
numVezes = 10
while numVezes - c != 0:
    while c < numVezes:
        print('{} '.format(inicio),  end='-> ')
        inicio = inicio + razão
        c += 1
    print('PAUSA')
    numVezes = int(input('Quantos termos você quer mostrar mais ? ')) + c
print('Progressão finalizada com {} termos mostrados.'.format(c))