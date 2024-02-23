x=0

resultado =0

while resultado != 46:
    x = int(input('digite o um valor para somar'))
    resultado = x + resultado
    print(' a soma ate agora  é ', resultado)
    if resultado == 46 :
        print('parabens vc acertou ')
    if resultado > 46 :
        print('vc passou do numero \n ')
        resultado = 0
        print ("digite sos valores novamente \n")

