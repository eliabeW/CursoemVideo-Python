'''
FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA
UM DOS DÍGITOS SEPARADOS.

EX: DIGITE UM NÚMERO: 1834

UNIDADE: 4
DEZENA: 3
CENTENA: 8
MILHAR: 1
'''

# Lê o número digitado pelo usuário e já garante que será tratado como texto (string)
n = str(input('Digite um número qualquer: '))

# Mostra o número que será analisado
print('Analisando o número {}'.format(n))

# Acessa cada dígito usando índices negativos (de trás pra frente)
print('Unidade: ', n[-1]) # último dígito
print('Dezena: ', n[-2])  # penúltimo dígito
print('Centena:', n[-3])  # antepenúltimo dígito
print('Milhar:', n[-4])   # primeiro dígito (em números de 4 algarismos)