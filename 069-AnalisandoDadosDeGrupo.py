cIda = mulheres =homens = 0
while True:
    print('-' * 30)
    print('CADASTRO DE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        cIda += 1
    sexo = ' '
    while sexo not in 'FfMm':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    print('-' * 20)
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    conti = ' '
    while conti not in 'SsNn':
        conti = str(input('Quer continuar ? [S/N]: ')).upper().strip()[0]
    if conti != 'S':
        break
print(f'Total de pessoas com mais de 18 anos: {cIda}\nAo todo temos {homens} homens\nE {mulheres} mulheres com menos de 20 anos')








