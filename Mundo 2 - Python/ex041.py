"""
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 20 anos: SENIOR
- acima: MASTER
"""

# Importa a função date para pegar o ano atual
from datetime import date
ano_atual = date.today().year

# Título do programa
print('-=-'*10)
print('CATEGORIAS DOS ATLETAS')
print('-=-'*10)

# Pede o ano de nascimento e calcula a idade
nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade = ano_atual - nascimento

# Até 9 anos: MIRIM
if idade <= 9:
    print('O atleta tem {} anos, categoria MIRIM.'.format(idade))
# De 10 a 14 anos: INFANTIL
elif idade <= 14:
    print('O atleta tem {} anos, categoria INFANTIL.'.format(idade))
# De 15 a 19 anos: JUNIOR
elif idade <= 19:
    print('O atleta tem {} anos, categoria JUNIOR.'.format(idade))
# De 20 anos: SENIOR
elif idade <= 20:
    print('O atleta tem {} anos, categoria SENIOR.'.format(idade))
# Acima de 20 anos: MASTER
else:
    print('O atleta tem {} anos, categoria MASTER.'.format(idade))