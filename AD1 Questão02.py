def numeroOcorrido():
    n = list(map(int, input().split()))
    ocor = 0
    valor = 0
    if len(n) != 0:
        for c in range(0, len(n)):
            if n.count(n[c]) > ocor:
                ocor = n.count(n[c])
                valor = n[c]
        print('Valor que mais ocorreu: {} que foi encontrado: {} vez(es)'.format(valor, ocor))
    else:
        print('nenhum número foi Lido !!!')
numeroOcorrido()