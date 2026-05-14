"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

# Cabeçalho visual do programa
print('-=' * 20)
print('Classificador de Triângulos')
print('-=' * 20)

# a, b, c: armazenam os comprimentos das três retas informadas pelo usuário
# São usados para verificar se formam um triângulo e qual o tipo
a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))

# Condição de existência do triângulo (desigualdade triangular):
# Cada lado precisa ser menor que a soma dos outros dois
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    # Classificação do tipo de triângulo com base na igualdade dos lados
    if a == b == c:
        # Equilátero: todos os três lados são iguais
        print('EQUILÁTERO (todos os lados iguais)')
    elif a != b != c != a:
        # Escaleno: todos os três lados são diferentes entre si
        print('ESCALENO (todos os lados diferentes)')
    else:
        # Isósceles: dois lados iguais e um diferente (qualquer outro caso)
        print('ISÓSCELES (dois lados iguais)')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo')
