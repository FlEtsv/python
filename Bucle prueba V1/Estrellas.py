anchura = 5
altura = 5
horizontal = 10
vertical = 10

for inicio in range(anchura*horizontal - horizontal +1): #inicio
    print('* ', end='')
print()

for cuerpo in range(vertical):#cuerpo
    if cuerpo % 2 == 0:
        for cuerpoContenido in range(altura - 2):
            for cuerpoInicio in range(horizontal):
                print('* ', end='')
                if cuerpoInicio % 2 == 0:
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
    
    for finalCuerpo in range(anchura*horizontal - horizontal + 1):
        print('* ', end='')
    print()