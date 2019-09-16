sal = float(input('Qual o salario do Funcionário  ?'))
reaj = sal + (sal * 15 / 100)
print('o funcionario ganhava R${:.2f},com o aumento de 15%, ele vai ganhar R${:.2f}'.format(sal, reaj))
