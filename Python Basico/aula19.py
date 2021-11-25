"""
36. Iterando strings com while em Python
Strings tem indices
"""
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_usuario = input('qual letra deseja colocar maiúscula: ')

#iteração
while contador < tamanho_frase:
    # print(frase[contador],contador)
    letra =  frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
