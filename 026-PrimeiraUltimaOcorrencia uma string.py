frase = str(input('Digite um nome ? ')).strip().upper()
print("A letra 'A' aparece {} vezes ".format(frase.count('A')))
print("A primeira letra 'A' apareceu na posição {}".format(frase.find('A') + 1))
print("A ultima letra aparece na posição 'A' {}".format(frase.rfind('A') + 1))

