"""
Quantidade de caractere-len
conta a quantidade de caractere em uma variavél string
"""
##Checagem de caractere do usúario 1
usuario = input('Digite seu usuario: ')
qtd_caractere = len(usuario)

if qtd_caractere < 6:
    print('Você precisa digitar pelo menos 6 caractere')
else:
    print('Você foi cadastrado no sistema')


##Checagem de caractere do usúario 2
string1 = input('Digite alguma coisa: ')
string2 = input('Digite alguma coisa: ')

print(f'A quantidade de total de caractere digitado foi {len(string1) + len(string2)} ')