n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segynda nota: '))
media = (n1 + n2) / 2
print('Com as notas {} e {}, a media é {}'.format(n1, n2, media))
if media >= 7:
    print('O aluno está APROVADO')
elif media < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está de Recuperação')
