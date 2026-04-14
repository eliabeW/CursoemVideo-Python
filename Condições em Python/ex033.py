'''FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.'''

n1 = int(input('Primeiro valor: '))  # Lê o primeiro número e converte para inteiro
n2 = int(input('Segundo valor: '))   # Lê o segundo número e converte para inteiro
n3 = int(input('Terceiro valor: '))  # Lê o terceiro número e converte para inteiro

# Bloco para encontrar o MAIOR número
if n1 > n2 and n1 > n3:        # Verifica se n1 é maior que os outros dois
    print('O maior valor digitado foi:', n1)
elif n2 > n1 and n2 > n3:      # Verifica se n2 é maior que os outros dois
    print('O maior valor digitado foi:', n2)
else:                           # Se nenhuma condição anterior for verdadeira, n3 é o maior
    print('O maior valor digitado foi:', n3)

# Bloco para encontrar o MENOR número
if n1 < n2 and n1 < n3:        # Verifica se n1 é menor que os outros dois
    print('O menor valor digitado foi:', n1)
elif n2 < n1 and n2 < n3:      # Verifica se n2 é menor que os outros dois
    print('O menor valor digitado foi:', n2)
else:                           # Se nenhuma condição anterior for verdadeira, n3 é o menor
    print('O menor valor digitado foi:', n3)