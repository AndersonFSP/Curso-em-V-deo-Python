
#for c in range(0, 20):
 #   print(f'2 elevado a {c} = {2 ** c}')

# lanche = ['hamburguer', 'Suco', 'Pizza', 'Pudim']# tuplas são imutáveis
# for c in lanche:
#     print(f'Eu vou comer {c}')
# print(sorted(lanche))
#
# a = (1,2,3,4)
# b = (3,4,5,2)
#
# for c in range(len(a)):
#     print(f'Soma de {a[c]} e {b[c]} é {a[c] + b[c]}')
# print(a.count(1))
# num =[1,2,3,4,5]
# num[1] = 98
# num.append(100)
# num.sort(reverse=True)
# num.insert(2, 15)
# num.pop()
# if 40 in num:
#     num.remove(40)
# print(num)
# for c in range(len(num)):
#     print(num[c], end=' ')
#
# for c, v in enumerate(num):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da Lista.')
# valores = list()
# for cont in range(0, 3):
#     valores.append(int(input(f'Digite o {cont+1} valor: ')))
# print(valores)
teste = list()

# teste.append('gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)
pessoas = [['joao', 19], ['Ana', 22], ['joaquim', 45], ['Maria', 21]]
# for p in pessoas:
#     print(p[1])
# for c in range(len(pessoas)):
#     print(f'{pessoas[c][0]} tem {pessoas[c][1]} de idade')
#
# turma = list()
# dado = list()
# for c in range(0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     turma.append(dado[:])
#     dado.clear()
# for c in range(len(turma)):
#     if turma[c][1] >= 20:
#         print(f'O {turma[c][0]} tem mais de 21')
turma = [['joao', 43], ['truw', 21]]
lista = []
for c in range(len(turma)):
    lista.append(turma[c][1])
print(max(lista))