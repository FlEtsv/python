from turtle import clear
condiNum = True        #Para poder ejecutar la funcion haasta recuperar una respuesta que nos sirva
print('realiza tu operacion, si quieres eliminar el ultimo numero escribe "remove"')
print('Si lo que quieres es eliminarlos todos y volver a introducir escribe "restart"')
print('Si has terminado de introducir datos pulsa t para calcular.')
while(condiNum):
    numeros = []          #lista que alamacena los numeros con los que se van a operar
    pedirNumeros = True   #Condicion para seguir pidiendo numeros
    N = 0 #contador
    while pedirNumeros:
        try:
            numeros = input(': ')
            #eliminar ultimo argumento de la lista
            
            #eliminar toda la lista y reiniciar el contador
            #hacer la operacion

            N += 1
        except:
            print('No introduzcas datos que no sean numeros')
    int(numeros)