"""
42. Enumerate - Tira dúvidas
"""

lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu'],
    ]

#enumerada = list(enumerate(lista))
#print(enumerada[1][0])

"""
[ <-- Enumerate

(0, ['Edu', 'João', 'Luiz']), 
(1, ['Maria', 'Aline', 'Joana']), 
(2, ['Helena', 'Ed', 'Lu'])

]
"""
for v1, v2 in enumerate(lista):
    print(v1, v2)

#dezempacotamento
for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)
