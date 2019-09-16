print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
inicio = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
c = 0
while c < 10 :
    print('{} '.format(inicio),  end='-> ')
    inicio = inicio + razão
    c += 1
print('Acabou')