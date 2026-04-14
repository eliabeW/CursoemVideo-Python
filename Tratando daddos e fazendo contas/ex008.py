'''
ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O
EXIBA CONVERTIDO EM CENTIMENTROS E MILIMETROS
'''

V = int(input('Uma distância em metros:'))
print('A medida de {}m corresponde a {}cm e {}mm '.format(V, V*100, V*1000))

# ---------------------------------------------------
'''
OPÇÃO USANDO VARIÁVEIS

media = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(' A medida de {}m corresponde a {}cm e {}mm '.format(media, cm, mm))
'''
