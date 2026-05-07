"""
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
print('-=-'*10)
print('ALISTAMENTO MILITAR')
print('-=-'*10)

# Importa a função date do módulo datetime para pegar o ano atual
from datetime import date

# Pega o ano atual do sistema
ano_atual = date.today().year

# Pede o ano de nascimento do usuário
ano = int(input('Digite seu ano de nascimento: '))

# Calcula a idade da pessoa
idade = ano_atual - ano

# Se a idade for menor que 18, ainda vai se alistar
if idade < 18:
    # Calcula quantos anos faltam para completar 18
    falta = 18 - idade
    print('Faltam {} anos para o alistamento'.format(falta))
# Se a idade for exatamente 18, está na hora de se alistar
elif idade == 18:
    print('Está na hora de se alistar')
# Se a idade for maior que 18, já passou do tempo
else:
    # Calcula quantos anos passaram desde que completou 18
    passou = idade - 18
    print('Já passaram {} anos do alistamento'.format(passou))