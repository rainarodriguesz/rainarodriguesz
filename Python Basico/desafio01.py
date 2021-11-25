"""
Criar variáveis para nome (str), idade(int)
Altura (float) e peso (float) de uma pessoa
criar variáveis com ano atual
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter o IMC da pessoa com duas casas decimais (peso e na altura da pessoa)
Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Raina'
idade = 21
altura = 1.74
peso = 64
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso/(altura ** 2)

print('{} tem idade {} anos, o IMC é {} é o ano de nascimento é {}'.format(nome, idade, imc, ano_nascimento))
print(f'{nome} tem {idade} de idade seu Imc é {imc:.2f} e o ano de nascimento é {ano_nascimento}')
