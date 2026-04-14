'''
Escreva um programa que pergunte a quantidade de Km percorridos por um
carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

dias = int(input('Quantos dias alugados?' ))
km = float(input('Quantos Km rodados?' ))
preco_a_pagar_dia = dias * 60
preco_a_pagar_km = km * 0.15
precofinal = preco_a_pagar_dia + preco_a_pagar_km


print('O total a pagar é de {:.2f}'.format(precofinal))


'''
RESOLUÇÃO DO VÍDEO:

dias = int(input('Quantos dias alugados?' ))
km = float(input('Quantos Km rodados?' ))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
'''

