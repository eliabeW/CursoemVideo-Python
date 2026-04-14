'''
FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO
CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O
COMPRIMENTO DA HIPOTENUSA.
'''

# Passo 1: Receber os dados do usuário
# Usamos float() porque os catetos podem ter números decimais (ex: 3.5)
C_o = float(input('Digite o valor do cateto oposto: '))
C_a = float(input('Digite o valor do cateto adjacente: '))

# Passo 2: Calcular a Hipotenusa usando o Teorema de Pitágoras (a² + b² = c²)
# 1. (C_a**2 + C_o**2) -> Elevamos os dois catetos ao quadrado e somamos.
# 2. ** 0.5            -> Elevamos o resultado da soma a meio (0.5).
# Lembre-se: elevar a 0.5 é o mesmo que tirar a RAIZ QUADRADA.
C_h = (C_a**2 + C_o**2) ** 0.5

# Passo 3: Exibir o resultado
# {:.2f} serve para mostrar apenas 2 casas decimais após a vírgula
print('A hipotenusa vai medir {:.2f}'.format(C_h))

'''
---------------------------------------------------------------
# RESOLUÇÃO DO VÍDEO


co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

---------------------------------------------------------------

# COM IMPORTAÇÃO DA CLASSE MATH

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)

---------------------------------------------------------------

'''