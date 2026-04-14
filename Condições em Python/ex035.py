'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
'''
print('-=-'*15)          # Imprime o separador '-=-' repetido 15 vezes para decorar a interface
print('Analisador de Triângulos')  # Exibe o título do programa
print('-=-'*15)          # Repete o separador para fechar o cabeçalho

a = float(input('Comprimento da primeira reta: '))   # Lê o comprimento da primeira reta e converte para decimal
b = float(input('Comprimento da segunda reta: '))    # Lê o comprimento da segunda reta e converte para decimal
c = float(input('Comprimento da terceira reta: '))   # Lê o comprimento da terceira reta e converte para decimal

# Verifica a condição matemática do triângulo:
# cada lado deve ser menor que a soma dos outros dois
if a < b + c and b < a + c and c < a + b:
    print('As retas FORMAM um triângulo!')     # Se as três condições forem verdadeiras, forma triângulo
else:
    print('As retas NÃO formam um triângulo!') # Se qualquer condição falhar, não forma triângulo