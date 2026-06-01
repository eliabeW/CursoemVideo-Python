# Obtém do usuário um número inteiro para calcular a tabuada
numero = int(input('Digite um número para ver sua tabuada: '))

# Imprime uma linha horizontal decorativa (12 traços)
print('-' * 12)

# Laço 'for' que repete de 1 até 10 (range(1, 11) gera 1, 2, 3, ..., 10)
for c in range(1, 11):
    # Exibe cada linha da tabuada no formato "N x C = RESULTADO"
    # Exemplo com numero=5 e c=3: "5 x 3 = 15"
    print(f'{numero} x {c} = {numero * c}')
