'''
FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO
'''

preco = float(input('Digite o valor do produto: R$'))
novo = preco - (preco * 5 / 100)
print('O produto custa R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))