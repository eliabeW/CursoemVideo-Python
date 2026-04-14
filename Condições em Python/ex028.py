'''
ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE
0 E 5 E PEÇA PARA O ÚSUARIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO
COMPUTADOR.

O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU
'''

import random
from time import sleep

print('-=-' * 20)                                    # Imprime um separador visual repetindo '-=-' 20 vezes
print('Vou pensar em um número entre 0 e 5')         # Apresenta o desafio ao usuário
print('-=-' * 20)                                    # Fecha o cabeçalho com outro separador

numero = random.randint(0, 5)                   # Sorteia e guarda um número inteiro aleatório entre 0 e 5

palpite = int(input('Em que número pensei? '))       # Lê o palpite do usuário e converte de string para inteiro
print('PROCESSANDO...')                              # Mensagem de suspense enquanto "processa"
sleep(3)                                             # Pausa a execução por 3 segundos antes de revelar o resultado

if palpite == numero:                                # Verifica se o palpite é igual ao número sorteado
    print('PARABÉNS! Você conseguiu me vencer!')     # Bloco executado quando o usuário acerta
else:                                                # Caso o palpite seja diferente do número sorteado...
    print('GANHEI! Eu pensei no número {}'.format(numero))  # Revela o número correto e declara vitória do computador