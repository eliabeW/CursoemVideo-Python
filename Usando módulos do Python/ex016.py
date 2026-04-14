'''
CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER
PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA.
'''

import math
num = float(input('Digite um número: '))
int = math.floor(num) #usando a função math floor, ele “arredondasse para baixo” até chegar em um número inteiro.
print('A porção inteira do número {}, é {}'.format(num, int))


