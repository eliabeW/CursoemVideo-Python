'''
FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:

- QUANTAS VEZES APARECE A LETRA "A".
- EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ.
- EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ.
'''

# Lê a frase, remove espaços extras e converte tudo para maiúsculas
# (assim encontra 'A' independente de como o usuário digitou)
frase = str(input('Digite uma frase: ')).strip().upper()

# Conta quantas vezes a letra 'A' aparece na frase
q = frase.count('A')
print('A letra "A", aparece {} vezes'.format(q))

# Encontra a posição da primeira ocorrência do 'A'
# O +1 ajusta para contagem humana (começa em 1, não em 0)
p = frase.find('A') + 1
print('A letra "A", aparece a primeira vez na posição {}'.format(p))

# Encontra a posição da última ocorrência do 'A'
# rfind() percorre a string de trás pra frente
u = frase.rfind('A') + 1
print('A letra "A", aparece a última vez {}'.format(u))