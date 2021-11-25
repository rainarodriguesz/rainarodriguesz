"""
Pythn é uma linguagem interepretada, tipagem dinâmica
Tipos de dados
str - string - textos "Assim" 'Assim'
int - inteiro - 123456 0 -10 - 20 -50
float - real/ponto flutuante  - 10.50 - 1.5 - - 10.10  - 1500 176879
bool - booleano/lógicon  - true/false   10 == 10 ? true
"""
print('alguma coisa')
print("Aspas duplas")
print(123445)
print("Essa é uma 'string' (str).")
print('Esse é meu \'texto\' (str).')   #caractere de scap
print(r'Esse é meu \n (str).')         #quebra de linha r
print('-----------------------------------------------')
print('Luiz', type('Luiz'), bool('Luiz'))  #retorna o tipo de dado e o dado boleano
print('10', type('10'), type(10))          #conversão de string para interiro
print(10, type(10))
print(25.34, type(25.34))
print('l' == 'l', type('l' == 'l'))
print(bool(0))

print('----------------------------')
#String: nome
print('Raina Rodrigues', type('Raina Rodrigues'))
#Int: idade
print(21, type(21))
#Float: altura
print(1.73, type(1.73))
#Maior de 18 anos
print(21 > 18, type(21 > 18))
