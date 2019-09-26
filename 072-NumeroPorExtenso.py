numerosExtenso = ('zero', 'um', 'dos', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


n = int(input('Digite um numero entre 0 e 20: '))
while (n > 20) or (n < 0):
    n = int(input('Tente novamente, digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {numerosExtenso[n]}')



