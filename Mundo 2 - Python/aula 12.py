nome = str(input("Qual é seu nome? ")) # Pede o nome do usuário e armazena na variável 'nome'

if nome == 'Eliabe': # Verifica se o nome é exatamente 'Eliabe'
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': # Verifica se o nome é um dos nomes populares masculinos/femininos
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jéssica Juliana':# Verifica se o nome está dentro da string (compara letra por letra)
    print('Belo nome feminino!')
else:                                      # Caso nenhum dos critérios acima seja atendido
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome)) # Exibe uma mensagem de despedida personalizada com o nome informado