''' FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO '''

from datetime import date  # Importa o módulo date da biblioteca datetime para trabalhar com datas

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))  # Lê o ano digitado pelo usuário e converte para inteiro

if ano == 0:  # Verifica se o usuário digitou 0
    ano = date.today().year  # Substitui o 0 pelo ano atual do sistema

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # Verifica as regras de ano bissexto:
                                                         # - Divisível por 4 E não divisível por 100
                                                         # - OU divisível por 400
    print('O ano {} é BISSEXTO'.format(ano))  # Exibe mensagem caso o ano seja bissexto
else:
    print('O ano {} Não é BISSEXTO'.format(ano))  # Exibe mensagem caso o ano não seja bissexto
