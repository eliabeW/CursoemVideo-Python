'''
FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA
O VALOR DO SENO, COSsENO E TANGENTE DESSE ÂNGULO.
'''
import math
a = float(input('Digite o valor do angulo: '))
r = math.radians(a)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)

print('O ângulo {} tem o SENO de {:.2f}'.format(a, s))
print('O angulo {} tem o COSSENO de {:.2f}'.format(a, c))
print('O angulo {} tem o TANGENTE de {:.2f}'.format(a, t))


