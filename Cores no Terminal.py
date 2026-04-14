'''
Style
0 - none
1 - bold (negrito)
4 - Underline (sublinhar)
7 - Negative (inverte)

------------------------------

# Text
30 - branco
31 - vermelho
32 - verde
33 - amarelo
34 - azul
35 - roxo
36 - ciano
37 - cinza

-------------------------------

# Back
40 - branco
41 - vermelho
42 - verde
43 - amarelo
44 - azul
45 - roxo
46 - ciano
47 - cinza
'''

nome = 'Elibe'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['azul'], nome, cores['limpa']))
