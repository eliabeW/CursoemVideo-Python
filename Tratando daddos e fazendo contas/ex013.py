'''
FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO,
COM 15% DE AUMENTO
'''

salario = float(input('Qual é o salário do Funcionário? R$ '))
novo_salario = salario + (salario * 15 / 100)

print('Um funcionario que ganhava {}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salario, novo_salario))