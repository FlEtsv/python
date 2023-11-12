"""
Hacer un patito centrado

"""
cabezaAnchura = 4
cabezaAltura = 3
cuelloAltura = 8
cuerpoAnchura = 10
cadena = '*'

def cabezaPatito():
    """
    cuadrado centrado que hace como cabeza
    """
    for cAl in range(0,cabezaAltura):
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
                if cuAl == 3 or cuAl == 7:
                    for cueAn in range(1):
                        cadena = '* * * * * * * * * *'
                        print(cadena.rjust(23), end='')
                    print()
                else:
                    for cueAn in range(1):
                        cadena = '*                 *'
                        print(cadena.rjust(23), end='')
                    print()
            else:       
                cadena = '* *'
                print(cadena.rjust(7))
#inicio de las funciones        

cabezaPatito()
cuello_cuerpo()
    