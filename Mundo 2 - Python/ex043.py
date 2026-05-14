"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 - 25: Peso Ideal
- Entre 25 - 30: Sobrepeso
- Entre 30 - 40: Obesidade
- Acima de 40: Obesidade mórbida

"""

# Cabeçalho visual do programa
print('-=' * 20)
print('{:=^40}'.format(' CALCULADOR DE IMC '))
print('-=' * 20)

# peso: armazena o peso do usuário em kg para o cálculo do IMC
peso = float(input('Qual o seu peso? (Kg) '))
# altura: armazena a altura do usuário em metros para o cálculo do IMC
altura = float(input('Qual a sua altura? (m) '))

# imc: calcula o Índice de Massa Corporal usando a fórmula peso / altura²
# altura * altura é o mesmo que altura ** 2 (ambos elevam ao quadrado)
imc = peso / (altura * altura)

print('Seu IMC é {:.1f}'.format(imc))

# Classifica o IMC de acordo com os intervalos da tabela da OMS
if imc < 18.5:
    # Abaixo de 18.5 significa peso abaixo do ideal
    print('Você está ABAIXO DO PESO normal')
elif imc >= 18.5 and imc <= 25:
    # Entre 18.5 e 25 é considerado peso saudável
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc >= 25 and imc <= 30:
    # Entre 25 e 30 indica excesso de peso
    print('Você está em SOBREPESO')
elif imc >= 30 and imc <= 40:
    # Entre 30 e 40 indica obesidade
    print('Você está em OBESIDADE!')
elif imc >= 40:
    # Acima de 40 é o caso mais grave (obesidade mórbida)
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
