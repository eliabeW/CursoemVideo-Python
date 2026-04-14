'''
CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU
NÃO COM O NOME "SANTO".
'''

# Lê o nome da cidade, remove espaços extras no início e no fim
cid = str(input('Em que cidade você nasceu: ')).strip()

# Pega os 5 primeiros caracteres, converte para maiúsculas e compara com 'SANTO'
# O print exibe True se a cidade começa com "Santo", ou False caso contrário
print(cid[:5].upper() == 'SANTO')
