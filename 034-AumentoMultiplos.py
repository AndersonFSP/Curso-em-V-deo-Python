sal = float(input('Digite o salário do funcionario? R$ '))
if sal <= 1000:
    reaj = sal + (sal * 15 / 100)
else:
    reaj = sal + (sal * 10 / 100)

print('O Salario de R${:.2f} reajustado será R${:.2f}'.format(sal, reaj))
