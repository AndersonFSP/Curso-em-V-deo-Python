info = []
ime = []
c = 0
while True:
    c += 1
    ime.append(str(input('Nome: ')))
    ime.append(float(input('Peso: ')))
    info.append(ime[:])
    ime.clear()
    resp = str(input('Deseja continuar ?')).upper()[0]
    if resp in 'Nn':
        break
print('=-' * 30)
for c in range(len(info)):
    ime.append(info[c][1])
# print(f'Ao todo foram cadastrados {c}')
# print(f'O maior peso cadastrado foi {max(ime):.1f}Kg. Peso de {info[ime.index(max(ime))][0]}') OPÇÃO MAIS LEGAL POREM SO MOSTRA UM NOME
# print(f'O menor peso cadastrado foi {min(ime):.1f}Kg. Peso de {info[ime.index(min(ime))][0]}')
print(f'O maior peso cadastrado foi {max(ime):.1f}kg. ', end='')
for c in range(len(info)):
    if info[c][1] == max(ime):
        print(info[c][0], end=' ')
print(f'\nO menor peso cadastrado foi {min(ime):.1f}kg. ', end='')
for c in range(len(info)):
    if info[c][1] == min(ime):
        print(info[c][0], end=' ')


