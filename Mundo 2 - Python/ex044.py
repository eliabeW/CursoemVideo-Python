"""
Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e a
condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão 20% de juros
"""
# Título e opções de pagamento
print('{:=^40}'.format(' LOJAS '))
print('Formas de pagamento: \n 1- À vista dinheiro/cheque (10% de desconto) \n 2- À vista no cartão (5% de desconto) \n 3- Em até 2x no cartão (Preço normal) \n 4- Em até 3x ou mais no cartão (20% de juros) ')

# Lê o valor do produto e a condição de pagamento
valor_produto = float(input('Qual o valor do produto: '))
cond_pag = str(input('Qual a condição de pagamento: '))

# Opção 1: à vista dinheiro/cheque - 10% de desconto
if cond_pag == '1':
    valor_produto = valor_produto * 0.9
    print('Valor do produto à vista dinheiro/cheque: R${:.2f}'.format(valor_produto))
# Opção 2: à vista no cartão - 5% de desconto
elif cond_pag == '2':
    valor_produto = valor_produto * 0.95
    print('Valor do produto à vista no cartão: R${:.2f}'.format(valor_produto))
# Opção 3: em até 2x no cartão - preço normal
elif cond_pag == '3':
    parcela = valor_produto / 2
    print('Valor do produto em até 2x no cartão: R${:.2f}, ficando 2x de R${:.2f}'.format(valor_produto, parcela))
# Opção 4: 3x ou mais no cartão - 20% de juros
elif cond_pag == '4':
    valor_produto = valor_produto * 1.2
    print('Valor do produto 3x ou mais no cartão, 20% de juros: R${:.2f}'.format(valor_produto))
# Opção inválida
else:
    print('Escolha uma das 4 opções')