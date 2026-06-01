"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.
"""

primeiro = int(input('Primeiro termo: '))  # lê o primeiro termo da PA
razao = int(input('Razão: '))  # lê a razão (valor somado a cada termo)

for n in range(10):  # repete 10 vezes para os 10 primeiros termos
    termo = primeiro + n * razao  # calcula o enésimo termo
    print(termo, end=' → ')  # exibe o termo na mesma linha
print('FIM')  # indica o fim da sequência
