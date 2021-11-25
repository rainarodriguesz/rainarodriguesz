"""
38. Listas em Python
fatiamento
append, insert, pop, del,clear,extend, + mim, max
range
"""

#         0    1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[0:3]) #mostra até o C
print(lista[:4])  #até o D
print(lista[:-1]) #Exclui o último
print(lista[::2]) #inicio ao fim, pulando de dois em dois
print(lista[::-1]) #invertendo a lista completa

print('---------Exemplos de extenssão de variavél extend/append--------------------')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
#l3 = l1 + l2  #adicionando os valores de forma manual
l1.extend(l2) #adicionou os valores de toda l2
l1.extend('a') #adicionou só um valor
l2.append('b') #adicionou só um valor
print(l1)
print(l2)
print(l2[3], 'valor adicionado no l2 \n') #imprindo o valor adicionado em b

print('---------Exemplos de extenssão de variavél insert--------------------')
l2.insert(0, 'banana') #inserindo no indice 0, banana
print(l2, '\n')


print('---------Exemplos de extenssão de variavél delet--------------------')
print('O valor de l2', l2)
del(l2[3:4])
print('Sem os valores excluidos', l2, '\n')

print('---------Exemplos de extenssão de variavél valores max--------------------')
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(max(a))  # somente valores inteiros
print(min(a))

print('--------- Lista --------------------')
b = list(range(1, 10))
print(b, '\n')    #retorna a lista

print('--------- Lista com for --------------------')
b_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for valor in b_2:
    print(valor, '\n')

print('--------- Lista soma --------------------')
b_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
soma = 0
for valor in b_2:
    soma = soma + valor
print(soma, '\n')

print('--------- Tipos de elementos --------------------')
l3 = ['String', True, 10, -10.4]

for elem in l3:
    print(f'O tipo de elemento é {type(elem)} e seu valor é {elem}, \n')

