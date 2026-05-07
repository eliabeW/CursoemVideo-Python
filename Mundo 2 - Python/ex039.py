"""
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:

-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do tempo do alistamento.
"""
from datetime import date
ano_atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano

if idade < 18:
    falta = 18 - idade
    print('Faltam {} anos para o alistamento'.format(falta))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    passou = idade - 18
    print('Já passaram {} anos para o alistamento'.format(passou))