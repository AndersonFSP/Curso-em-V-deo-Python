quant = 0
resp = 'a'
media = 0
soma = 0
maiorNumero = 0
while resp != '':
    resp = input()
    if resp != '':
        resp = float(resp)
        soma += resp
        quant += 1
        if resp > maiorNumero:
            maiorNumero = resp
media = soma / quant

print('Quantidade de números: {}'.format(quant))
print('Média de números: {:.2f}'.format(media))
print('Maior: {}'.format(maiorNumero))
