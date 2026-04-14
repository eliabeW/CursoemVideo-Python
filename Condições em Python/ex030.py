'''CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA ELE É PAR OU ÍMPAR'''

numero = int(input('Digite um número inteiro: '))  # Lê o número digitado pelo usuário e converte para inteiro

if numero % 2 == 0:  # Verifica se o resto da divisão por 2 é zero (condição para ser par)
    print('Par')  # Se o resto for zero, o número é par
else:
    print('Impar')  # Se o resto for diferente de zero, o número é ímpar