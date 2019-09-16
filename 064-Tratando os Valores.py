soma = c = nume = 0
while nume != 999:
    nume = int(input('Digite um valor [999 para parar]: '))
    if nume != 999:
        soma += nume
        c += 1
print('Você digitou {} numeros Soma dos numros é {} '.format(c, soma))