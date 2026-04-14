'''
FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA
O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.

EX: ANA MARIA DE SOUZA
PRIMEIRO = ANA
ÚLTIMO = SOUZA
'''

nome = str(input('Digite seu nome completo: ')).strip() # Lê o nome e remove espaços extras nas bordas
print('Muito prazer em te conhecer!')  # Mensagem de boas-vindas
primeiro = nome.split()[0] # Divide o nome em partes e pega a primeira (índice 0)
print('Seu primeiro nome é {} '.format(primeiro)) # Exibe o primeiro nome
ultimo = nome.split()[-1] # Divide novamente e pega a última parte (índice -1)
print('Seu último nome é {} '.format(ultimo)) # Exibe o último nome

# ------------------------------------------------------------------------
#SOLUÇÃO DO PROFESSOR

'''
n = str(input('Digite seu nome completo: ')).strip()      # Lê o nome completo e remove espaços extras nas bordas
nome = n.split()                                          # Divide o nome em uma lista de partes (ex: ['Ana', 'Maria', 'de', 'Souza'])
print('Muito prazer em te conhecer!')                     # Mensagem de boas-vindas
print('Seu primeiro nome é {} '.format(nome[0]))          # Acessa o índice 0 da lista — sempre o primeiro nome
print('Seu último nome é {} '.format(nome[len(nome)-1]))  # len(nome)-1 retorna o índice do último elemento da lista
'''