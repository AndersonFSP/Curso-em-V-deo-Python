list = [[0, 0, 0], [0, 0, 0], [0, 0, 0 ]]
aux = []
somaPares = somaColuna = maiorLinha =  0
for c in range(0, 3):
    for l in range(0, 3):
        list[c][l] = int(input(f'Digite um valor [{c},{l}]: '))
print('-=' * 30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[ {list[c][l]:^5} ]', end='')
        if c == 1 and list[c][l] > maiorLinha:
            maiorLinha = list[c][l]
        if list[c][l] % 2 == 0:
            somaPares += list[c][l]
        if l == 2:
            somaColuna += list[c][l]
    print()
print('-=' * 30)
print(f'A soma dos valores pares {somaPares}\nA soma da terceira coluna {somaColuna}\nO maior numero da segunda linha {maiorLinha}')
