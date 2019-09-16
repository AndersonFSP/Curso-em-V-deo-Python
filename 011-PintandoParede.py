Largura = float(input('Largura da parede: '))
Altura = float(input('Altura da parede: '))
area = Largura * Altura
print('Sua parede tem dimensao de {:.2f} X {:.2f} e sua area é de: {}m²'.format(Largura, Altura, area))
print('Para pintar a parede é necessário {:.2f}l de tinta. '.format(area/2))


