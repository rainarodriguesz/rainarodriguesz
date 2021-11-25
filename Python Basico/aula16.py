"""
Indice de fatiamentpo de Strings - Manipulando string 34
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print,etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""

#Acessando caracteres de uma variavel - positivos [012345678]
a = 'Python s2'
print(a[5]) #acessando só a posição 5 da variavél
print(a[2:6]) #acessando só a posição 2 até a 5 da variavél(fatiamento de string)
print(a[:6]) #acessando só a posição inicial da variavél até a 5 da variavél(fatiamento de string)
print(a[:6]) #acessando só a posição inicial da variavél até a 5 da variavél(fatiamento de string)
b = 'Raina Rodrigues'
print(b[0:10:2]) #acessando só a posição inicial da variavél até a 10 e pula 2 dois em dois caractere da variavél
print(b[:]) #pegar a string toda


#Acessando caracteres de uma variavel - negativos [987654321]
a = 'Python s2'
print(a[-9:-5]) #acessando só a posição até outra da variavél
print(a[:-1]) #acessando a posição inicial até o penultimo caractere

url = 'www.google.com.br/'
print(url[:-1])
