"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
"""
from datetime import datetime
ano_atual = datetime.now().year  # pega o ano atual do sistema

maiores = 0  # contador de maiores de idade
menores = 0  # contador de menores de idade

for n in range(7):  # repete 7 vezes
    ano = int(input('Digite o ano de nascimento: '))  # lê o ano de nascimento
    idade = ano_atual - ano  # calcula a idade
    if idade >= 21:  # se for maior de idade
        maiores += 1
    else:  # se for menor de idade
        menores += 1

print(f'{maiores} pessoa(s) são maior(es) de idade')
print(f'{menores} pessoa(s) são menor(es) de idade')
