casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos deve pagar: '))

prestacao = casa / (anos * 12)

print('Emprestimo vai ser de R${:.2f}'.format(prestacao))
if prestacao > (sal * 30 ) / 100:
    print('Emprestimo negado')
else:
    print('Emprestimo aceito')