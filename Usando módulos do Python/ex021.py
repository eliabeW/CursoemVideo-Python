'''
FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO
DE UM ARQUIVO MP3.
'''

import pygame
# Inicializa o mixer (específico para áudio)
pygame.mixer.init()

# Carrega o arquivo (certifique-se de que o arquivo está na mesma pasta do .py)
pygame.mixer.music.load('ex021.mp3')

# Dá o play
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)