valores=[]
while True:
    n = int(input('Digite Um valor: '))
    valores.append(n)
    resp = str(input('Deseja continuar [S/N]: ')).upper().split()[0]
    if resp == 'N':
        break
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'A lista na orderm descrescente{valores}')
if 5 in valores:
    print('O valor 5 foi encontrado ')
else:
    print('O valor 5 não foi encontrado na lista')