"""
Operadores Relacionais
== > >= < <= !=
"""

print("----------Teste com números----------")
num_1 = 2
num_2 = 2
expressao = (num_1 > num_2)
print(expressao)

print("----------Teste com String----------")
var_1 = 'Luiz'
var_2 = 'Otavio'
expressao_2 = var_1 == var_2
print(expressao_2)

print("----------Teste----------")
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
idade_min = int(18)

if idade >= idade_min:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} não pode pegar o emprestimo.')
