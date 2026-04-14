'''
FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE
DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA ÁREA DE 2m²
'''

L = float(input('Largura da parede: '))
A = float(input('Altura da parede: '))
area = L*A
t = area / 2


print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisará de {}l de tinta.'.format(L, A, area, t))

