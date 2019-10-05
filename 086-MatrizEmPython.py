list = [[0, 0, 0], [0, 0, 0], [0, 0, 0 ]]
aux = []
for c in range(0, 3):
    for l in range(0, 3):
        list[c][l] = int(input(f'Digite um valor [{c},{l}]: '))
print('-=' * 30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[ {list[c][l]} ]', end='')
    print()