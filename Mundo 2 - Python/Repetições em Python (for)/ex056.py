"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

A média de idade do grupo.
Qual é o nome do homem mais velho no grupo.
Quantas mulheres tem menos de 20 anos.
"""

somaidade = 0  # Acumulador para somar as idades
maioridadehomem = 0  # Armazena a maior idade entre os homens
nomevelho = ''  # Armazena o nome do homem mais velho
qtdmulh = 0  # Contador de mulheres com menos de 20 anos

for n in range(4):  # Laço para ler os dados de 4 pessoas
    nome = str(input('Digite o seu nome: ')).strip()  # Lê o nome e remove espaços
    idade = int(input('Digite sua idade: '))  # Lê a idade
    sexo = str(input('Digite o seu sexo: ')).strip()  # Lê o sexo e remove espaços
    somaidade += idade  # Soma a idade ao acumulador
    if sexo in 'Mm' and idade > maioridadehomem:  # Se for homem e idade maior que a atual
        maioridadehomem = idade  # Atualiza a maior idade masculina
        nomevelho = nome  # Atualiza o nome do homem mais velho
    if sexo in 'Ff' and idade < 20:  # Se for mulher e tiver menos de 20 anos
        qtdmulh += 1  # Incrementa o contador de mulheres

media = somaidade / 4  # Calcula a média de idade do grupo

print(f'A média de idade do grupo é de {media} anos.')  # Exibe a média
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')  # Exibe o homem mais velho
print(f'Ao todo temos {qtdmulh} mulher(es) com menos de 20 anos.')  # Exibe a quantidade de mulheres