"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
"""

# Título do programa
print('-'*40)
print('APROVADOR DE EMPRÉSTIMO BANCÁRIO')
print('-'*40)

# Pergunta o valor da casa, o salário e em quantos anos vai pagar
valor_casa = float(input('Qual o valor da casa? R$' ))
salario = float(input('Qual seu salário? R$' ))
anos = int(input('Quantos anos deseja pagar? '))

# Calcula o valor da prestação mensal (preço da casa dividido pelos meses)
prestacao = valor_casa / (anos * 12)
# Calcula 30% do salário (limite máximo permitido para a prestação)
limite = salario * 0.30

# Mostra o valor da casa e o valor da prestação
print('Para pagar uma casa de R${:.2f} em {} anos,'.format(valor_casa, anos))
print('A prestação será de R${:.2f}'.format(prestacao))

# Se a prestação for menor ou igual a 30% do salário, aprova
# Senão, nega o empréstimo
if prestacao <= limite:
    print('Empréstimo pode ser Aprovado!')
else:
    print('Empréstimo Negado!')




