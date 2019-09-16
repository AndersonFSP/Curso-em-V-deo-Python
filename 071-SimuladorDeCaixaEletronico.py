proxN = c = 0
numeroCedulas = [None] * 0
valoresCedulas =[None] * 0
arrayCedulas =[50, 20, 10, 5, 1]
print('='*20)
print('BANCO BIZARRO')
print('='*20)
valor = int(input('Qual valor você quer sacar ? '))
while True:
    if proxN == 0:
        while arrayCedulas[proxN] > valor:
            proxN += 1
        resto = valor % arrayCedulas[proxN]
        incremento = valor // arrayCedulas[proxN]
        numeroCedulas.append(incremento)
        incremento = arrayCedulas[proxN]
        valoresCedulas.append(incremento)
    else:
        resto = resto % arrayCedulas[proxN]
    if resto == 0:
        break
    else:
        while arrayCedulas[proxN] > resto:
            proxN += 1
        incremento = resto // arrayCedulas[proxN]
        numeroCedulas.append(incremento)
        incremento = arrayCedulas[proxN]
        valoresCedulas.append(incremento)
for c in range(len(numeroCedulas)):
    print(f'Total de {numeroCedulas[c]} cédulas de {valoresCedulas[c]} reais')
print('====================================\nVolte Sempre!!!!!')




