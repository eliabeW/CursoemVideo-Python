'''
CRIE UM PROGRAMA QUE LEIA O NOME DE UMA  PESSOA E DIGA SE ELA
TEM "SILVA" NO NOME.
'''

nome = str(input('Qual é seu nome completo: ')).strip().title()
mod = 'Silva' in nome

print(mod)