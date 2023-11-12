"""
hecho por Steven
15/12/22
18:59

"""
print('pulsa 1 para poner las medidas del tablero.')
strEleccion = input('pulsa 2 para hacer un tablero estandar: ')
try:
    eleccion = int(strEleccion)
    if eleccion != 1:
        anchura = 5
        altura = 5
        horizontal = 10
        vertical = 10

        for inicio in range(anchura*horizontal - horizontal +1): #inicio
            print('* ', end='')
        print()

        for cuerpo in range(vertical):#cuerpo
            if cuerpo % 2 == 0:#condicion alternas tipos de linea
                for cuerpoContenido in range(altura - 2):
                    for cuerpoInicio in range(horizontal):
                        print('* ', end='')
                        if cuerpoInicio % 2 == 0:#condicion alternar en la misma linea
                            for cuerpoColor in range(anchura - 2):
                                print('  ', end='')
                        else:
                            for cuerpoColor in range(anchura - 2):
                                print('* ', end='')
                    print('* ')
            else:
                for cuerpoContenido in range(altura - 2):
                    for cuerpoInicio in range(horizontal):
                        print('* ', end='')
                        if cuerpoInicio % 2 == 0:
                            for cuerpoColor in range(anchura - 2):
                                print('* ', end='')
                        else:
                            for cuerpoColor in range(anchura - 2):
                                print('  ', end='')
                    print('* ')
            
            for finalCuerpo in range(anchura*horizontal - horizontal + 1):#final
                print('* ', end='')
            print()
    else:
        print('no have falta que sea cuadrado. puedes hacer rectangulos')
        strAnchura = input('ancho de los cuadrados: ')
        strAltura = input('altura de los cuadrados: ')
        strHorizontal = input('numero de cuadrados en horizontal(ancho en cuadrados)')
        strVertical = input('numero de cuadrados en vertical(altura en cuadrados)')
        try:
            anchura = int(strAnchura)
            altura = int(strAltura)
            horizontal = int(strHorizontal)
            vertical = int(strVertical)
            
            for inicio in range(anchura*horizontal - horizontal +1): #inicio
                print('* ', end='')
            print()

            for cuerpo in range(vertical):#cuerpo
                if cuerpo % 2 == 0:#condicion alternas tipos de linea
                    for cuerpoContenido in range(altura - 2):
                        for cuerpoInicio in range(horizontal):
                            print('* ', end='')
                            if cuerpoInicio % 2 == 0:#condicion alternar en la misma linea
                                for cuerpoColor in range(anchura - 2):
                                    print('  ', end='')
                            else:
                                for cuerpoColor in range(anchura - 2):
                                    print('* ', end='')
                        print('* ')
                else:
                    for cuerpoContenido in range(altura - 2):
                        for cuerpoInicio in range(horizontal):
                            print('* ', end='')
                            if cuerpoInicio % 2 == 0:
                                for cuerpoColor in range(anchura - 2):
                                    print('* ', end='')
                            else:
                                for cuerpoColor in range(anchura - 2):
                                    print('  ', end='')
                        print('* ')
                
                for finalCuerpo in range(anchura*horizontal - horizontal + 1):#final
                    print('* ', end='')
                print()
        except:
            print('Intentalo de nuevo')
except:
    print('Solo entiendo el numero 1 o el numero 2.')