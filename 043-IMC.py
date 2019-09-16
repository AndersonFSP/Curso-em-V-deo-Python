peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sual altura (m): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25 and imc >= 18.5:
    print('Peso ideal')
elif imc < 30 and imc >=25:
    print('Sobrepeso')
elif imc < 40 and imc >=30:
    print('Obesidade')
else:
    print('Obesidade Morbida')