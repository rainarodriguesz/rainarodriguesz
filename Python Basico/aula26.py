"""
Dezempacotamento de listas em Python

"""
lista = ['Luiz', 'João', 'Maria']
n1, n2, n3 = lista
print(n2)

print('---------------Ultimos valores------------------')

lista2 = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 100]
m1, m2, *outras_lista, ultimo_lista = lista2
print(ultimo_lista)

