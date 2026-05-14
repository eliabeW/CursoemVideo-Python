"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0;
REPROVADO
- Média entre 5.0 e 6.9;
RECUPERAÇÃO
-Média 7.0 ou superior;
APROVADO
"""
# Título do programa
print('-=-'*10)
print('Analisador de notas de um aluno')
print('-=-'*10)

# Lê as duas notas do aluno
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
# Calcula a média aritmética
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
# Média abaixo de 5.0: REPROVADO
if media < 5.0:
    print('REPROVADO')
# Média entre 5.0 e 6.9: RECUPERAÇÃO
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
# Média 7.0 ou superior: APROVADO
else:
    print('APROVADO')