from datetime import date
anoAtual = date.today()
nasc = int(input('Ano de nascimento: '))
idade = anoAtual.year - nasc
print('O atleta tem {} anos'.format(idade))
categoria = ''
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14 and idade > 9:
    categoria = 'INFANTIL'
elif idade <=19 and idade > 14:
    categoria = 'JUNIOR'
elif idade == 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('CATEGORIA: {}'.format(categoria))


