'''
ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR
DO SEU AUMENTO.

PARA SALÁRIOS SUPERIORES A R$1.250,00 , CALCULE UM AUMENTO DE 10%.

PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%
'''

salario = float(input('Qual é o salário do funcionário? R$'))  # Lê o salário do funcionário e converte para decimal

if salario <= 1250:            # Verifica se o salário é inferior ou igual a R$1.250,00
    aumento = salario * 1.15   # Calcula o novo salário aplicando 15% de aumento
else:                          # Caso o salário seja superior a R$1.250,00
    aumento = salario * 1.10   # Calcula o novo salário aplicando 10% de aumento

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, aumento))  # Exibe o salário antigo e o novo formatados em reais

# ----------------------------------------------------------------------------------------------------------
# Solução do Professor
'''
salario = float(input('Qual é o salário do funcionário? R$'))  # Lê o salário do funcionário e converte para decimal

if salario <= 1250:                        # Verifica se o salário é inferior ou igual a R$1.250,00
    novo = salario + (salario * 15 / 100)  # Calcula o aumento de 15% e soma ao salário original
else:                                      # Caso o salário seja superior a R$1.250,00
    novo = salario + (salario * 10 / 100)  # Calcula o aumento de 10% e soma ao salário original

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, novo))  # Exibe o salário antigo e o novo formatados em reais

'''