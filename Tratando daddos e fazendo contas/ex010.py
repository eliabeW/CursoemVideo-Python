'''
CRIE UM PROGRAMA QUE LEIA QUANTO DE DINHEIRO
UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS
DÓLARES ELA PODE COMPRAR.

CONSIDERE: US$1,00 = R$ 3,27
'''

carteira = float(input('Digite o valor da carteira: R$'))
carteira = carteira / 3.27
print('Você pode comprar US${:.2f}'.format(carteira))

