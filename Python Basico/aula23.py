"""
40. FOR / ELSE em Python

"""
variavel = ['Luiz Otávio', 'joãozinho', 'Maria']
comeca_com_j = False

print('---Exemplo de código que encontra uma palavra que começa com determinada letra------')
for valor in variavel:
    if valor.lower().startswith('j'):  # converte pra minusculo e verificando se a variavél começa com J
        comeca_com_j = True
        print('Começa com J ', valor)
        break
else:
    print('Não existe uma palavra que começa com J')

print('---Excluindo a palavra que começa com J---')
for x in variavel:
    if x.lower().startswith('j'):  # converte pra minusculo e verificando se a variavél começa com J
        continue
    print(x)
