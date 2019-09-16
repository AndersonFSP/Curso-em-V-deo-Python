soma = c = 0

while True:
    n = int(input('Digite um numero (999 para)'))
    if n == 999:
        break
    soma += n
    c += 1
print(f'Digitou {c} numeros, a soma foi {soma}')



