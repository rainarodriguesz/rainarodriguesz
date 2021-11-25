"""
34. While - estrutura de repetição em Python
Ultilizando para realizar ações enquanto uma condição for verdadeira
"""
'''
while True:
    nome = input("Qual seu nome?")
    print(f'olá{nome}')

print('Essa experessão não será exercutada')

break - finaliza o loop
continue - continua exercutando o loop

'''


'''
x = 0
while x < 10:
    if x == 3:
        print(x)
        x = x + 2
        break

    print(x)
    x = x+1
print('Acabou')
'''

'''
x = 0 #coluna
y = 0 #linha

while x < 10:
    y = 0
    while y < 5:
        #print(f'x vale {x} e y vale {y}')
        print(f'{x},{y}')
        y += 1

    x += 1 #x = x + 1

print('acabou')
'''
#Calculadora
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s] sim ou [n] não: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digite apenas numeros!')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador invalido!')
