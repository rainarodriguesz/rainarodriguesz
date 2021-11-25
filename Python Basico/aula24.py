"""
41. Split, Join e Enumerate em Python
Split - Dividoir uma string # str
Join - Juntar uma lista # str
Enumerate - Enumerar elementos da lista # list / itaráveis
"""
string = 'O Brasil é o pais do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',') #Separar frases
print('----------Adicionando espaço na frase------------')
print(lista_1, '\n')
print('----------Adicionando virgula na frase--------------')
print(lista_2, '\n')

print('----------Formatando a saída dos valores--------------')
for valor in lista_2:
    print(valor.strip().capitalize()) #Remover o espaço ini e fim - Deixar a primeira deltra maiúsculo

print('----Quantidade de vezes que a palavra a apareceu na frase----')
for valor in lista_1:
    print(f'A palavra: {valor} apareceu {lista_1.count(valor)}x na frase.')
print('\n')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem: #contando qual palavra apareceu mais vezes
        contagem = qtd_vezes
        palavra = valor

print('---------------------------------------------------')
print(f'A palavra que apareceu mais vezes é {palavra}')


#Juntando a lista dentro da string
string1 = 'O Brasil é penta.'
lista = string1.split(' ') #Separar o texto por partes
string2 = ','.join(lista) #junta com virgula e transformando uma lista em uma string
print('---------------------------------------------------')
print(string1)
print(lista)
print(string2, '\n')

#Enumereite
string1 = 'O Brasil é penta.'
lista = string1.split(' ') #Separar o texto por partes

print('-- Enumerando as partes das frase --')
for id, valor in enumerate(lista):
    print(id, valor)  #enumera cada valor

print('------Lendo as colunas-------------')
a = [
    [1, 2],
    [3, 4],
    [5, 6],
]
for v in a:
    print(v[0], v[1], '\n')

print('---------Função Enumerate----------')
b = [
    [1, 'Luiz'],
    [3, 'João'],
    [5, 'Maria'],
]
for id, nome in b:
    print(id, nome)

print('---------Função Enumerate 2----------')
c = ['Luiz', 'João', 'Maria']
n1, n2, n3 = c
print(n2)


