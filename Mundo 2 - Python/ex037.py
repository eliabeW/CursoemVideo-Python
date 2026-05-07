# Pede um número inteiro ao usuário
numero = int(input('Digite um número inteiro: '))
# Pede para escolher a base de conversão (1, 2 ou 3)
base_conversao = int(input('Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n '))

# 1 = Binário: usa bin() e remove os dois primeiros caracteres ('0b')
if base_conversao == 1:
    print(f'{numero} convertido para binário = {bin(numero)[2:]}')
# 2 = Octal: usa oct() e remove os dois primeiros caracteres ('0o')
elif base_conversao == 2:
    print(f'{numero} convertido para octal = {oct(numero)[2:]}')
# 3 = Hexadecimal: usa hex() e remove os dois primeiros caracteres ('0x')
elif base_conversao == 3:
    print(f'{numero} convertido para hexadecimal = {hex(numero)[2:]}')
# Se digitar qualquer outra opção, mostra mensagem de erro
else:
    print('Opção invalida, tente novamente.')
