"""
39. Tira dúvidas: for, listas, condições e concatenações

"""

secreta = 'Python'
secreto_temp = ''
digitadas = ['t']

for letra_secreta in secreta: #esse for vai percorrer cada indice da letra secreta, lendo cada letra de um por um
    print(f'Interação para a letra {letra_secreta}')

    if letra_secreta in digitadas: #ler o primeiro indice P e verifica se a letra digitada e a = a letra secreta
        print(f'Eba, a letra que eu queria {letra_secreta}')
        secreto_temp += letra_secreta #adiciona a letra na variavél final
    else:
        secreto_temp += '*'
print(secreto_temp)
