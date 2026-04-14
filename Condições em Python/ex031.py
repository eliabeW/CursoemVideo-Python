'''
DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0.50 POR KM PARA VIAGENS DE ATÉ 200KM E R$0.45 PARA
VIAGENS MAIS LONGAS.
'''

distancia = float(input("Qual a distância da viagem em Km: "))  # Lê a distância digitada pelo usuário e converte para decimal
print('Você está prestes a começar uma viagem de {:.2f} Km.'.format(distancia))  # Exibe a distância formatada com duas casas decimais

if distancia <= 200:  # Verifica se a viagem tem até 200km
    distancia = distancia * 0.50  # Calcula o preço cobrando R$0,50 por km
    print('E o preço da sua passagem será de R${:.2f}'.format(distancia))  # Exibe o preço formatado em reais
else:  # Caso a viagem seja maior que 200km
    distancia = distancia * 0.45  # Calcula o preço cobrando R$0,45 por km
    print('E o preço da sua passagem será de R${:.2f}'.format(distancia))  # Exibe o preço formatado em reais
