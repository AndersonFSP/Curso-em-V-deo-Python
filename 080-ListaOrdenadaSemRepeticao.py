lista= []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Adcionado ao final da Lista')
    else:
        if n >= max(lista):
            lista.append(n)
            print('Adcionado ao final da Lista')
        elif n <=min(lista):
            lista.insert(0, n)
            print(f'adicionado a posição {lista.index(n)} da lista')
        else:
            if c == 2:
                lista.insert(1, n)
                print(f'adicionado a posição {lista.index(n)} da lista')
            else:
                if n > min(lista) and n <= lista[2]:
                    lista.insert(1, n)
                    print(f'adicionado a posição {lista.index(n)} da lista')
                if n < max(lista) and n >= lista[2]:
                    lista.insert(4, n)
                    print(f'adicionado a posição {lista.index(n)} da lista')
print('=-' * 30)
print(f'Os valores digitados foram {lista}')