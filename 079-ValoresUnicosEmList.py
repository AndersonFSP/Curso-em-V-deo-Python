valores = []
while True:
    n = int(input('Digite Um valor: '))
    if n in valores:
        print('Esse numero existe, não será adicionado:')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso !!')
    resp = str(input('Deseja continuar [S/N]: ')).upper().split()[0]
    if resp == 'N':
        break
print('=-'*30)
valores.sort()
print(f'Você digitou os valores {valores}')






