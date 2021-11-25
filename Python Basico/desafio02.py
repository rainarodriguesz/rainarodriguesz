"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o úsuario não diguite um número
inteiro, informe que não é um número inteiro.

num_int = input('Digite um numero: ')

if num_int.isdigit():
    num_int = int(num_int)
    if num_int % 2 == 0:
        print(f'{num_int} é par')
    else:
        print(f'{num_int} é impar')
else:
    print(num_int, " Não é inteiro")
"""


"""
Faça um programa que pergunte a hora ao usuário e,baseando-se no 
horário descrito, exiba a saudação apropriada.
Ex: Bom dia 0-11, Boa tarde 12-17 e boa noite 18-23.  

horario = input('Digite a hora de (0-23): ')

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print("Horario deve está entre 0 e 23")
    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print(horario," Não é inteiro, digite um horário entre 0 e 23")
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é  curto", se tiver entre 5 e 6 letras, escreva "Seu 
nome é normal", maior que 6 escreva "seu nome é muito grande".
"""

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho<= 4:
    print("Seu nome é curto")
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')

