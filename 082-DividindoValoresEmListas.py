valores = []
pares = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    resp = str(input('Deseja continuar ? [S/N] ')).upper().split()[0]
    if resp == 'N':
        break
print('=-' * 20)
print(f'A lista é completa é {valores}')
for c in range(len(valores)):
    if valores[c] % 2 == 0:
        pares.append(valores[c])
    else:
        impar.append(valores[c])
print(f'A lista de pares é {pares}\nA lista de impares é {impar}')
