"""
Hecho por Steven
30/12/2022
"""

#funciones del patito

def cabezaPatito(cabezaAltura, cabezaAnchura):
    """
    bucle de creacion de cuadrado, en el que se incluye un ojo
    pico estatico dentro de cada recorrido del mismo cuadrado
    """ 
    for cAl in range(0,cabezaAltura):#recorrido vertical
        if cAl == 0:
            print('      * ', end='')#pico
            for cAn in range(0,cabezaAnchura):#recorridos horizontales
                print('* ', end='')
            print()
        if cAl == 1:
            print('    * * ', end='') 
            for cAn in range(0,cabezaAnchura):
                if cAn == 0:
                    print('[]', end='')
                    continue
                print('* ', end='')
            print()
        if cAl == 2:
            print('  * * * ', end='')
            for cAn in range(0,cabezaAnchura):
                print('* ', end='')
            print()
        if cAl == 3:
            print('* * * * ', end='')  
            for cAn in range(0,cabezaAnchura):
                print('* ', end='')
            print()


def cuello_cuerpo(cuelloAltura):
    """
    el cuello y cuerpo del patito
    centrado para que concuerde con lacabeza
    """
    for cuAl in range(cuelloAltura):
        for cuAn in range(1):
            if cuAl > 2:
                if cuAl == 3:
                    for cueAn in range(1):
                        cadena = '* * * * * * * * * * * *'
                        print(cadena.rjust(33), end='')#centrado
                    print()
                elif cuAl == 4:
                    for cueAn in range(1):
                        cadena = '*       **        * *'
                        print(cadena.rjust(31), end='')
                    print()
                elif cuAl == 5:
                    for cueAn in range(1):
                        cadena = '*       ****  *   *'
                        print(cadena.rjust(29), end='')
                    print()    
                elif cuAl == 6:
                    for cueAn in range(1):
                        cadena = '*       *******   *'
                        print(cadena.rjust(29), end='')
                    print()
                elif cuAl == 7:
                    for cueAn in range(1):
                        cadena = '* * * * * * * * * *'
                        print(cadena.rjust(29), end='')
                    print()
                elif cuAl == 10:
                    for cueAn in range(1):
                        cadena = '    **  **         '
                        print(cadena.rjust(29), end='')
                    print()
                else:
                    for cueAn in range(1):
                        cadena = '     *   *         '
                        print(cadena.rjust(29), end='')
                    print()
            else:       
                cadena = '* *'
                print(cadena.rjust(13))

#Menu eleccion dibujo

def eleccionVariables():
    """
    Permite elegir a traves de numeros las diferentes opciones disponibles
    """
    global nom
    nom = input('¿Como me dirijo a ti? ')
    print(f'pulsa 1 para dibujar un patito {nom}.') #menu inicial de eleccion
    print('pulsa 2 para hacer un tablero estandar.')
    strEleccion = input('O pulsa 3 para hacer un arbol de navidad: ')
    try:#excepcion del menu
        global eleccion
        eleccion = int(strEleccion)
    except:
        print('Solo entiendo numeros de momento')

#funciones del cuadrado de ajedrez

def cuerpoBucle(anchura , altura, horizontal, vertical):
    """
    Tablero de ajedrez
    ejecuta un bucle de inicio y de final
    el contenido es una serie de bucles relacionados con la anchura, altura de cada cuadrado 
    y a su vez relacionado con el numero de repeticiones verticales y horizontales de cada cuadrado

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

#arbol de navidad

def tamañoArbol():
    """
    Multiplicador de tamaño con una variable llamada Tamaño
    Evita el error de tamaño por encima de los niveles establecidos 
    """
    global Tamaño
    print('Los tamaños van de 1 al 3.')
    Tamaño = int(input('Que tamaño quieres el arbol?'))
    if Tamaño < 4:
        if Tamaño == 1:
            Tamaño
        elif Tamaño % 2 != 0:
            Tamaño = Tamaño + 1
    else:
        print('De momento solo tenemos 3 niveles de tamaño') 
        for tam in range(Tamaño,4,-1):
            Tamaño -= 1
    
    


def arbolNav(tamañoTronco, tamañoHojas):
    """
    crea un arbol de navidad centrado en 30
    usa una funcion suma continua a traves de un contador
    """
    tamañoTronco = tamañoTronco * Tamaño
    tamañoHojas = tamañoHojas* Tamaño

    for hojas in range(1,tamañoHojas,2):
        print(('^'*hojas).center(30*Tamaño))

    for tronco in range(tamañoTronco):
        print(('|||').center(30*Tamaño))
    print(('\_____/').center(30*Tamaño))



#Despedida

def Despedida(anchura):
    """
    Realiza un dialogo de despedida breve
    rodeado de lineas basadas en caracteres que siguen su longitud
    """
    cadena = 'Gracias por confiar en nosotros '
    cadena += nom
    puntitos = len(cadena)
    for desp in range(anchura):
        for desp2 in range(puntitos):
            print('*', end='')
        print()
    print(f'{cadena}!')
    for desp3 in range(anchura):
        for desp4 in range(puntitos):
            print('*', end='')
        print()


#aqui empieza la llamada a las funciones








eleccionVariables()
if eleccion == 1:
    cabezaPatito(4, 3)
    cuello_cuerpo(11)

elif eleccion == 2:
    cuerpoBucle(4,4,10,10)
elif eleccion == 3:
    tamañoArbol()
    arbolNav(1,30)
else: 
    print('No tenemos disponible esa figura de momento.')
Despedida(2)