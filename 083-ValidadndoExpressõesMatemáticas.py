expressoes = []

exp = str(input('Digite a espresão: '))
for c in range(len(exp)):
    expressoes.append(exp[c])

if expressoes.count('(') == expressoes.count(')'):
    print('Expressão válida')
else:
    print('Expressão Inválida')
