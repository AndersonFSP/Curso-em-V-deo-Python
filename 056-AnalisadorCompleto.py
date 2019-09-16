totIdade = 0
maiorIdade = 0
totMuie = 0
for c in range(1, 5):
    print('---- {}o PESSOA ----'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F]').upper().strip()
    lista = [nome, idade, sexo]
    totIdade += lista[1]
    if lista[2] == 'M' and lista[1] > maiorIdade:
        maiorIdade = lista[1]
        nomeVelho = lista[0]
    if lista[2] == 'F' and lista[1] < 20:
        totMuie += 1
Media = totIdade / 4
print('A média de idade do grupo é de {:.1f} anos'.format(Media))
print('O homem mais velho tem {}anos e se chama {}'.format(maiorIdade, nomeVelho))
if totMuie > 0:
    print('Ao todo são {} mulheres com menos de 20 anos'.format(totMuie))




