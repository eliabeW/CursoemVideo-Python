"""
Faça um programa que leia um número inteiro e diga se ele é ou não primo.
"""

num = int(input('Digite um número: '))  # lê o número a ser verificado

divisores = 0  # contador de divisores

for n in range(1, num + 1):  # testa divisão por todos os números de 1 até num
    if num % n == 0:  # se a divisão for exata
        divisores += 1  # incrementa o contador

if divisores == 2:  # primo tem exatamente 2 divisores (1 e ele mesmo)
    print(f'{num} é primo')
else:
    print(f'{num} não é primo')
