def mdc(a, b):
    anterior = a
    atual = b
    resto = anterior % atual
    while resto != 0:
        anterior = atual
        atual = resto
        resto = anterior % atual
    print(atual)


while True:
    entrada = list(map(int, input().strip().split()))
    if(entrada[0] and entrada[1] < 0 ):
        break
    mdc(entrada[0], entrada[1])