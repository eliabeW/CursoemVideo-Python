"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

# Cabeçalho
print('-=' * 20)
print('Classificador de Triângulos')
print('-=' * 20)

# Leitura dos três segmentos
a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))

# Condição de existência do triângulo (desigualdade triangular)
if a < b + c and b < a + c and c < a + b:
    # Classificação do tipo de triângulo
    if a == b == c:
        print('EQUILÁTERO - todos os lados iguais')
    elif a == b or b == c or c == a:
        print('ISÓSCELES - dois lados iguais')
    else:
        print('ESCALENO - todos os lados diferentes')
else:
    print('As retas NÃO formam um triângulo')
