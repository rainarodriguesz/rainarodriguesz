"""
Documentação e função built-in úteis
isnumeric - checar números e positivos(12345);
isdigit, isdecimal
"""
"""
Função ISNUMERIC
num1 = input('Digite um numero: ')
num2 = input('Digite outro numero ')

num1 = int(num1)
num2 = int(num2)

print(num1.isnumeric())
print(num2.isnumeric())
"""
# -----------------------------------------------------------
"""
num1 = input('Digite um numero: ')
num2 = input('Digite outro numero ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print("Não pude converter os numeros para realizar contas ")
"""
# -----------------------------------------------------------
num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print("ERROR")

"""
import re

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero ')

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
else:
    print('Error')
"""
