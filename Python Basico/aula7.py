"""

"""

nome = 'Luiz ótavio'
idade = 23
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso/(altura ** 2)


print(nome, 'tem', idade, 'de idade seu Imc é ', imc)
print(f'{nome} tem {idade} de idade seu Imc é {imc}')  #a saida é a mesma
print(f'{nome} tem {idade} de idade seu Imc é {imc:.2f}') #Mostra apenas duas casas decimais
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
##-------------------Paramentros enumerados e nomeados-----------------
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))