'''
CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:

- O NOME COM TODAS AS LETRAS MAIÚSCULAS
- O NOME COM TODAS AS LETRAS MINÚSCULAS
- QUANTAS LETRAS AO TOTAL (SEM CONSIDERAR ESPAÇOS)
- QUANTAS LETRAS TEM O PRIMEIRO NOME.
'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome me minúsculo é {}'.format(nome.lower()))
print('Seu primeiro nome tem {} letras'.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))