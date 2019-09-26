valores = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))

print(f'Você digitou os valores {valores}')
print(f"O valor 9 apareceu {valores.count(9)}")
if valores.count(3) == 0:
    print('O valor 3 não foi digitado')
else:
    print(f'O valor 3 aparece na posição {valores.index(3)}')
print('Os valores pares foram: ', end='')
for c in range(len(valores)):
    if valores[c] % 2 == 0:
        print(valores[c], end=' ')

