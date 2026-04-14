'''
UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATROS ALUNOS PARA APAGAR O QUADRO.
FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO
ESCOLHIDO.
'''

import random
# 1. Lendo os nomes
aluno_1 = input('Primeiro aluno: ')
aluno_2 = input('Segundo aluno: ')
aluno_3 = input('Terceiro aluno: ')
aluno_4 = input('Quarto aluno: ')

# 2. Criando a "sacola" (Lista)
# Colocamos as variáveis dentro de colchetes [] para criar uma lista
sacola = [aluno_1, aluno_2, aluno_3, aluno_4]

# Escolhe um item diretamente da lista
escolhido = random.choice(sacola)

# 4. Exibindo o resultado
print('O aluno escolhido foi {}'.format(escolhido))