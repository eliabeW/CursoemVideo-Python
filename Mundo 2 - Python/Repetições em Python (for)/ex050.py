"""
Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.
"""

soma = 0  # acumulador para somar os números pares
for n in range(6):  # loop que se repete 6 vezes
    num = int(input('Digite um número: '))  # lê um número inteiro
    if num % 2 == 0:  # verifica se o número é par
        soma += num  # se for par, adiciona à soma
print(f'A soma dos números pares é: {soma}')  # exibe o resultado