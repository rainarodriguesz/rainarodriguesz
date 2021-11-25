"""
32. Formatando valores em Python
Formatando valores com modificadores - Aula 5
:s - texto (string)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(numero) f-quantidade de casas decimais(float)
:(caractere)(> ou < ^)(quantidade/tipo - s, d ou f)

> - Esquerda
< - Direta
^ - Centro
"""
num_1 = 10
num_2 = 1500
div = (num_1 / num_2)

print(f'{num_1:0>10} formatado para a esquerda')
print(f'{num_1:0<10} formatado para a direita')
print(f'{num_1:0^10} formatado para o centro')

print('{:.2}'.format(div))

'''Duas casas decimal com o zero'''
print(f'{num_2:.2f} adiciona duas casas decimais com 0, no numero {num_2}')
print('------------------------------------------------------')
'''  Combinar os valores '''
nome = "Raina"
'''
nome_formatado= '{:@>5}'.format(nome)
nome_formatado= '{}'.format(nome)
nome_formatado_pn= '{n}'.format(n=nome)  paramentros nomeados
nome_formatado= '{n:0<20}'.format(n=nome)
'''
sobrenome = "Rodrigues"
nome_formatado = '{0:$^50}\n{1:#^50}'.format(nome,sobrenome) #formatar só o sobre nome
print(nome_formatado)
print(sobrenome.lower()) #tudo minusculo
print(sobrenome.upper()) #tudo maiusculo
print(sobrenome.title()) #Com as primeiras letras maiuscula
