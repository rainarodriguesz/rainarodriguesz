"""
45. Operação ternária em Python
"""

# #Checagem se é maior de idade 1
# idade = 18
#
# if idade >= 18:
#     print('Pode acessar')
# else:
#     print('Não pode acessar')

idade = input('Qual a sua idade?')



if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
    print(msg)


#Checagem de login 1
# logged_user = False
# msg = 'Usuário Logado!' if logged_user else 'Usuário precisa logar'
# print(msg)


#Checagem de login 2
# if logged_user == True:
#     msg = 'Usuário Logado!'
# else:
#     msg = 'Usuário precisa logar'
# print(msg)
