'''
O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO
DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS
E MOSTRE A ORDEM SORTEADA
'''

import random

# 1. Entrada de Dados
# Lemos os nomes dos quatro alunos através do teclado

aluno_1 = input('Primeiro aluno: ')
aluno_2 = input('Segundo aluno: ')
aluno_3 = input('Terceiro aluno: ')
aluno_4 = input('Quarto aluno: ')

# 2. Criação da Lista
# Agrupamos as variáveis dentro de colchetes [] para criar uma "lista" (ou sacola)
# A ordem inicial aqui não importa, pois vamos embaralhar
sacola = [aluno_1, aluno_2, aluno_3, aluno_4]

# 3. O Embaralhamento (Shuffle)
# O comando shuffle NÃO CRIA uma lista nova, ele REORGANIZA a lista 'sacola'
# É por isso que não fazemos "ordem = random.shuffle", pois ele retornaria None
random.shuffle(sacola)

# 4. Exibição do Resultado
# Agora que a lista 'sacola' já teve sua ordem trocada internamente,
# nós a exibimos completa dentro da frase.
print('A ordem de apresentação será: {}'.format(sacola))