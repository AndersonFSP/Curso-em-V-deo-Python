def mapeiaString(palavra, alvos):
    numDeAlvos = 0
    for c in range(len(palavra)):
        if palavra[c] in alvos:
            numDeAlvos += 1
    return numDeAlvos


def medePalavra(palavra):
        return len(palavra)

maiorNumDigitosPalavra = ''
somenteMinusculas=0
cont = 0
while True:
    palavra = str(input('digite: '))
    if palavra == '':
        break
    cont += 1
    tamanho = medePalavra(palavra)
    if cont == 1:
        maiorStr = palavra
        maiorNumDigitos = 0
    if tamanho > len(maiorStr):
        maiorStr = palavra
    numDigitos = mapeiaString(palavra, '0123456789')
    if(numDigitos >= maiorNumDigitos and numDigitos != 0 ):
        maiorNumDigitos = numDigitos
        maiorNumDigitosPalavra = palavra
    numMinusculas = mapeiaString(palavra, 'aeiou')
    if (numMinusculas == len(palavra)):
        somenteMinusculas += 1


if cont <= 0:
    print('Nenhuma String Não Vazia Foi Lida!!!')
else:
    print(f'Primeira de maior comprimento: {maiorStr}\nUltima com mais digitos: {maiorNumDigitosPalavra}\n'
          f'Quantidade de strings apenas Com Vogais Minúsculas {somenteMinusculas}')
