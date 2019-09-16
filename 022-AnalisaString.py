nome = str(input('Digite seu nome: ')).strip()
nomesplitado = nome.split()
print('Analisando seu nome ...')
print('Seu nome em Maiusculo é {}'.format(nome.upper()))
print('Seu nome em Minusculo é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomesplitado[0], len(nomesplitado[0])))

