"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até
0, com uma pausa de 1 segundo entre elas.
"""

from time import sleep  # Importa a função sleep para fazer a pausa de 1 segundo entre eles

# range(início, fim_exclusive, passo)
# range(10, -1, -1) -> começa em 10, decrementa de 1 em 1 até parar no 0 (pq -1 é exclusive)
for c in range(10, -1, -1):
    print(c)       # Exibe o número atual da contagem
    sleep(1)       # Pausa de 1 segundo entre cada número

# Mensagem final após o fim da contagem
print('FELIZ ANO NOVO!')