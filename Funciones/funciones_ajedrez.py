
def eleccionVariables():
    """
    Permite elegir a traves de numeros una de las opciones disponibles
    """
    print('pulsa 1 para dibujar un patito') #menu inicial de eleccion
    strEleccion = input('pulsa 2 para hacer un tablero estandar: ')
    try:#excepcion del menu
        global eleccion
        eleccion = int(strEleccion)
    except:
        print('Solo entiendo numeros de momento')



def cuerpoBucle(anchura, altura, horizontal, vertical):
    """

    El cuerpo de rectangulo

    """

    for inicio in range(anchura*horizontal - horizontal + 1): #inicio
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
        for inicio in range(anchura*horizontal - horizontal + 1): #inicio
            print('* ', end='')
        print()
#aqui empieza la llamada a las funciones








eleccionVariables()

cuerpoBucle(4,4,10,10)


