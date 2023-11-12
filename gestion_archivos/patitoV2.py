"""
Hacer un patito centrado

"""
def variable_patito():
    global cabezaAnchura
    global cabezaAltura
    global cuelloAltura
    global cuerpoAnchura

    cabezaAnchura = 3
    cabezaAltura = 4
    cuelloAltura = 11
    cuerpoAnchura = 10

def cabezaPatito():
    """
    cuadrado centrado que hace como cabeza
    """ 
    for cAl in range(0,cabezaAltura):
        if cAl == 0:
            print('      * ', end='')
            for cAn in range(0,cabezaAnchura):
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
def cuello_cuerpo():
    """
    dibuja cuello y hace sentencia 
    para empezar con el cuerpo
    """
    for cuAl in range(cuelloAltura):
        for cuAn in range(1):
            if cuAl > 2:
                if cuAl == 3:
                    for cueAn in range(1):
                        cadena = '* * * * * * * * * * * *'
                        print(cadena.rjust(33), end='')
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

#inicio de las funciones        

variable_patito()
cabezaPatito()
cuello_cuerpo()
    