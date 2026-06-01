"""
Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e a
condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão 20% de juros
"""
# Exibe o cabeçalho da loja centralizado em 40 caracteres
print('{:=^40}'.format(' LOJAS ELIABE '))

# Solicita o preço do produto ao usuário
preço = float(input('Qual o valor do produto: R$ '))

# Exibe as opções de condição de pagamento
print('''FORMAS DE PAGAMENTO: 
[ 1 ] À vista dinheiro/cheque (10% de desconto) 
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] Em até 2x no cartão (Preço normal)
[ 4 ] Em até 3x ou mais no cartão (20% de juros) ''')

# Captura a opção escolhida pelo usuário
opção = int(input('Qual a condição de pagamento: '))

# Aplica a condição de pagamento escolhida
if opção == 1:
    # À vista dinheiro/cheque: 10% de desconto
    # preço * 10 / 100  → calcula 10% do valor original
    # preço - (desconto) → subtrai o desconto do preço
    total = preço - (preço * 10 / 100)
elif opção == 2:
    # À vista no cartão: 5% de desconto
    # preço * 5 / 100   → calcula 5% do valor original (ex: 100 * 5 / 100 = 5)
    # preço - 5         → subtrai os R$5 de desconto (ex: 100 - 5 = 95)
    total = preço - (preço * 5 / 100)
elif opção == 3:
    # Em até 2x no cartão: preço normal (sem desconto ou juros)
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    # 3x ou mais no cartão: 20% de juros sobre o valor total
    # preço * 20 / 100  → calcula 20% de juros (ex: 100 * 20 / 100 = 20)
    # preço + 20        → soma os R$20 de juros ao preço (ex: 100 + 20 = 120)
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    # Opção inválida
    total = 0
    print('\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')

# Exibe o valor final da compra
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))
