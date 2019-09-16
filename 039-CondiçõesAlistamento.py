from datetime import date
anoAtual = date.today()
nasc = int(input('Ano de nascimento: '))
idade = anoAtual.year - nasc
print('Quem nasceu em {} vai ter {} anos em {}'.format(nasc, idade, anoAtual.year))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade ))
    print('Seu alistamento será em {}'.format( anoAtual.year + (idade - 18)  ))
else:
    print('Você ja deveria ter se alistado hà {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(anoAtual.year - (idade - 18)))
