resp = 'S'
soma = c = maior = menor =  0
while resp == 'S':
    n = int(input('Digite um numero: '))
    resp = str(input('Quer continuar ? [S/N] ')).upper().strip()
    soma += n
    if c < 1:
        menor = n
    c += 1
    if n > maior:
        maior = n
    elif n < maior and n < menor :
        menor = n


print('Você digitou {} numeros e a médida foi {:.2f} \nO maior valor foi {} e menor foi {}'.format(c, soma / c, maior, menor))
