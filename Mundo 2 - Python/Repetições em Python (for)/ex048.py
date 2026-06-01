"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram
no intervalo de 1 a 500
"""
soma = 0  # Inicializa a variável soma com 0 para ir acumulando os valores

# range(1, 501, 2) -> começa em 1, vai até 500, pulando de 2 em 2 (números ímpares: 1, 3, 5, 7...)
for n in range(1, 501, 2):
    # n % 3 == 0 verifica se o resto da divisão de n por 3 é zero (ou seja, n é múltiplo de 3)
    if n % 3 == 0:
        soma += n  # Se for múltiplo de 3, adiciona o valor de n à variável soma (soma = soma + n)

# Exibe o resultado total da soma
print(soma)
