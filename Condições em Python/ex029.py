'''
ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.

SE ELA ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE
FOI MULTADO.

A MULTA VAI CUSTAR R$ 7,00 POR KM ACIMA DO LIMITE.
'''

velocidade = int(input('Qual a velocidade atual do carro? '))  # Lê a velocidade digitada pelo usuário e converte para inteiro

if velocidade > 80:  # Verifica se a velocidade ultrapassa o limite de 80km/h
    excesso = velocidade - 80  # Calcula quantos km/h acima do limite o motorista está
    multa = excesso * 7  # Multiplica o excesso por R$7,00 para obter o valor da multa
    print('Você foi multado! Você excedeu o limite permitido que é de 80km/h \n'
          'Você deve pagar uma multa de R${:.2f}!'.format(multa))  # Exibe a mensagem de multa com o valor formatado em reais
else:
    print('Tenha um bom dia! Dirija com segurança')  # Caso esteja dentro do limite, exibe mensagem positiva