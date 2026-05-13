"""
Crie um programa que faça o computador jogar jokenpô com você.
"""
# Importa módulos necessários
from random import randint
from time import sleep

# Título e opções do jogo
print('{:=^40}'.format(' VAMOS JOGAR? '))
print('Escolha um dos três símbolos: \n[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura')

# Tupla com as opções
itens = ('Pedra', 'Papel', 'Tesoura')
# Computador escolhe aleatoriamente (0, 1 ou 2)
computador = randint(0, 2)
# Jogador faz sua escolha
jogador = int(input('Qual é a sua jogada? '))

# Contagem regressiva para dar suspense
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)

# Mostra as jogadas
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

# Verifica o resultado
if computador == jogador:
    # Mesma jogada: empate
    print('EMPATE!')
elif (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
    # Pedra ganha de Tesoura, Papel ganha de Pedra, Tesoura ganha de Papel
    print('COMPUTADOR VENCE!')
else:
    # Jogador ganha
    print('JOGADOR VENCE!')
