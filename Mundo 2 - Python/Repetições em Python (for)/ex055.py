"""
Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""

maior = 0  # maior peso inicial
menor = 0  # menor peso inicial

for n in range(5):  # repete 5 vezes
    peso = int(input('Digite o seu peso: '))  # lê o peso
    if n == 0:  # na primeira vez, maior e menor recebem o primeiro peso
        maior = menor = peso
    else:  # nas demais vezes, compara e atualiza
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso foi {maior}kg')
print(f'O menor peso foi {menor}kg')
