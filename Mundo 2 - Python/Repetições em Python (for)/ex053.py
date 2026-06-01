"""
Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços.
"""

frase = input('Digite uma frase: ').strip().upper()  # lê a frase, remove espaços extras e deixa em maiúsculo
palavras = frase.split()  # separa a frase em palavras
junto = ''.join(palavras)  # junta tudo sem espaços

inverso = ''  # string vazia para armazenar o inverso

for letra in range(len(junto) - 1, -1, -1):  # percorre do último caractere até o primeiro
    inverso += junto[letra]  # adiciona cada caractere ao inverso

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:  # compara o original sem espaços com o inverso
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
