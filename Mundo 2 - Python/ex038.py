"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

# Título do programa
print('-=-'*10)
print('COMPARADOR DE NÚMEROS')
print('-=-'*10)

# Lê dois números inteiros do usuário
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

# Compara os dois números e mostra qual é maior
if n1 > n2:
    print('O primeiro valor é maior')
elif n1 < n2:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')

