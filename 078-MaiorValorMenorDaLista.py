num = list()
for c in range(0,5):
    num.append(int(input(f'Digite o valor na posicao {c}: ')))
print('=-' * 30)
print(f'Os valores digitados foram {num}')
print(f'O maior valor digitado foi {max(num)} na posicao: ', end='')
for c in range(len(num)):
    if num[c] == max(num):
        print(f'{c}.. ', end='')
print(f'\nO menor valor digitado foi {min(num)} na posicao: ', end='')
for c in range(len(num)):
    if num[c] == min(num):
        print(f'{c}.. ', end='')

