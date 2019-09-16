vel = float(input('Qual a velocidade do carro ? '))
if vel > 80 :
    multa = (vel - 80) * 7
    print('Você foi multado, passou de 80 Km/h !! \n Deverá pagar R${:.2f}'.format(multa))
else:
    print('Você está abaixo da velocidade limite ')

print('Tenha um bom dia !')