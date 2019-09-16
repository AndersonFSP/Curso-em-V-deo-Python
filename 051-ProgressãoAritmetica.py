print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
inicio = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for c in range(inicio, (inicio + (10 - 1) * razão) + razão, razão):
    print('{} '.format(c),  end='-> ')
print('Acabou')