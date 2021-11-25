"""
37. For in - Estrutura de repetição em Python
For in em Python
Interando strings com for
Função range (start=0, stop, step=1)
"""
'''
Interação de strings com o laço for
texto = 'Python'

# c= 0
# while c < len (texto):
#     print(texto[c])
#     c += 1

# for letra in texto:
#     print(letra)   #imprimi os valores de um a um

for n, letra in enumerate (texto):
    print(n, letra)
'''

# # Função range - criar range de numeros
# # for numero in range(10):  #start=0,stop=10, step=1 padrão
# #     print(numero)    # conta de 0 até 9
#
# for numero in range(2,11,2): #recebe 3 argumentos
#     print(numero)
#
# print('--------------------------------------------------')
#
# for n in range (100):
#     if n % 8 == 0:  #resto da divisão - multiplo de 8
#         print(n)


#continue - pula para a proxima interação
#break - para a interação

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
