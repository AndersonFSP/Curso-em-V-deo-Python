v = input('Digite um valor : ')


print('O tipo primitivo do valor digitado é', type(v))
print('Só tem espaços', v.isspace())
print('É número ?', v.isnumeric())
print('É alfabético ?', v.isalpha())
print('É alfanumerico ?', v.isalnum())
print('É maiusculo ?', v.isupper())
print('É minusculo ?', v.islower())
print('É capitalizada', v.istitle())
