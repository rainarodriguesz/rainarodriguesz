"""
Operadores Lógico
end, or , not
"""
print('-----------------------Teste 1--------------------')

a = 2
b = 1

if b > a:
    print("B é maior que A")
else:
    print("A é maior")

if not b > a:
    print("A é maior que B")
else:
    print("B é maior")

print('-----------------------Teste 2--------------------')

c = ''
d = 0 ##zero também é um boleano falso

if not c:
    print('Por favor preencha o valor de c')

nome = 'Luiz Otávio'

if 'fd' in nome:
    print("Existe a letra u no seu nome.")
else:
    print('Não existe.')


print('-----------------------Teste 3: validação de usuário-------------------')

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'luiz'
senha_bd = '123456'
if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado')
else:
    print('Usuário ou senha inválidos')
