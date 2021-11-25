"""
Input: Entrada de dados do Usúario
"""

'''
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_nascimento = 2019 - int(idade)

print()
print(f'{nome} tem anos {idade} e o ano de nascimento é {ano_nascimento}') 
'''
# Problema: Não soma porque está recebedo valores inteiros
# numero_1 = input('digite o numero 1')
# numero_2 = input('digite o numero 2')
# print(numero_1 + numero_2)

#A soma dos numero só é feita depois que que é convertido para int
numero_1 = int(input('digite o numero 1 '))
numero_2 = (input('digite o numero 2 '))
numero_2 = int(numero_2)
print(numero_1 + numero_2)
