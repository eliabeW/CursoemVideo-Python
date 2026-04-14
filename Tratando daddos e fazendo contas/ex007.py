'''
DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO,
CALCULE E MOSTRE A SUA MÉDIA.
'''

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
r = (n1 + n2) / 2

print('A média entre {} e {} é igual a {}'.format(n1, n2, r))