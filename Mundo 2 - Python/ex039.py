"""
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

# Exibe o cabeçalho do programa
print('-=-'*10)
print('ALISTAMENTO MILITAR')
print('-=-'*10)

# Importa a função date do módulo datetime para pegar o ano atual
from datetime import date

# ano_atual: armazena o ano corrente para poder calcular a idade do usuário
ano_atual = date.today().year

# ano: guarda o ano de nascimento informado pelo usuário para ser usado no cálculo da idade
ano = int(input('Digite seu ano de nascimento: '))

# idade: calcula quantos anos a pessoa tem (ou terá no fim do ano) para comparar com os 18 anos obrigatórios
idade = ano_atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, ano_atual))

# Verifica se a pessoa tem exatamente 18 anos (deve se alistar agora)
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')

# Verifica se a pessoa tem menos de 18 anos (ainda vai se alistar)
elif idade < 18:
    saldo = 18 - idade  # saldo: anos que faltam para completar 18 (prazo restante)
    print('Ainda faltam de {} anos para o alistamento'.format(saldo))
    ano = ano_atual + saldo  # ano: ano previsto para o alistamento futuro
    print('Seu alistamento sera em {}'.format(ano))

elif idade > 18:
    saldo = idade - 18  # saldo: anos que passaram desde que completou 18 (atraso)
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = ano_atual - saldo  # ano: ano em que o alistamento deveria ter ocorrido
    print('Seu alistamento foi em {}'.format(ano))
