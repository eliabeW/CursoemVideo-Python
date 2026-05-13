"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 - 25: Peso Ideal
- Entre 25 - 30: Sobrepeso
- Entre 30 - 40: Obesidade
- Acima de 40: Obesidade mórbida

"""

# Cabeçalho
print('-=' * 20)
print('{:=^40}'.format(' CALCULADOR DE IMC '))
print('-=' * 20)

# Leitura dos dados do usuário
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))

# Cálculo do IMC
imc = peso / (altura * altura)

print('Seu IMC é {:.2f}'.format(imc))

# Classificação do IMC conforme a tabela
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
