"""
Hecho por Steven
Calculadora con funciones y colecciones
11:00 am
12/01/23
"""


#Funciones Menu
def menu():
  """
  bucle si la funcion es correcta lo cierra
  pregunta el nombre
  imprime un saludo mas el nombre dado
  """
  condicion ='true'
  while(condicion=='true'):
    nombre = input('hola dime tu nombre para saber como llamarte: ')
    totalCaracteres = len(nombre)
    if totalCaracteres > 0:
      break
  print(f'Encantado de poder ayudarte {nombre}')
  
def decoracionMenu():
  for puntitos in range(0,1):
    for puntos in range(0,40):
      print('*', end='')
  print()

def menueleccion():#implementacion de un diccionario en la calculadora.
  """
  eleccion entre las distintas operaciones poniendo explicitamente la palabra que representa dicha operacion.
  cuarda el resultado en una variable global
  """
  global ValNum
  ValNum = 0
  eleccion = dict[str:int]
  eleccion = {'suma':1, 'resta':2, 'multiplicacion':4, 'division':3}
  print('Escribe la operación que quieres hacer.')
  print('"suma" para sumar.')
  print('"resta" para restar.')
  print('"multiplicacion" para multiplicar.')
  print('"division" para dividir')
  eleccionDef = input('¿Que operacion quieres hacer?: ')
  if eleccionDef in eleccion:
    for clave, valor in eleccion.items():
      if clave == eleccionDef:
        ValNum += valor
        
  else:
    print('No entiendo lo que me quieres decir :(')

#funciones Numericas

def pedirNum():
  """
  Pide un numero que es guardado en una lista
  """
  global numeros2
  numeros2 = []             #lista que alamacena los numeros con los que se van a operar STR
  condiNum = True        #Para poder ejecutar la funcion haasta recuperar una respuesta que nos sirva
  print('realiza tu operacion, si quieres eliminar el ultimo numero escribe "delete".')
  print('Si lo que quieres es eliminarlos todos y volver a introducir escribe "clean".')
  print('Si has terminado de introducir datos pulsa "continue" para calcular.')
  while(condiNum):
    pedirNumeros = True   #Condicion para seguir pidiendo numeros
    while pedirNumeros:
      N = 0 #contador
      numeros = input(': ')
      if numeros == 'delete':
        numeros2.pop(N-1)
        N -=1
        print('la lista actual es: ', end='')
        for numL in numeros2:
          print(f'{numL},',end='')
        continue
      if numeros == 'clean':
        numeros2.clear()
        print('Empezamos de nuevo!!')
        continue
      if numeros == 'continue':
        break
        condiNum = False
      try:
        numeros3 = int(numeros) #mediador para que los datos sean de tipo INT
        numeros2.append(numeros3)#lista definitiva INT
      except:
        print('Porfavor introduce solo numeros.')
      N += 1
    break 



def sumam():
  """
  suma N1 con N2 y su resultado lo suma con N3...
  devuelve total de todas las operaciones
  """
  global totalsuma
  totalsuma = numeros2[0]       #igualamos para poder calcular con ello
  NumerosCalculos = len(numeros2)
  for operacion in range(1,NumerosCalculos):
    totalsuma += numeros2[operacion]
  return totalsuma
  

def restar():
  global totalresta
  """
  Resta N1 entre N2 y su total le resta N3....
  y devuelve el resultado
  """
  totalresta = numeros2[0]
  NumerosCalculos = len(numeros2)
  for operacion in range(1,NumerosCalculos):
    totalresta -= numeros2[operacion]
  return totalresta
  

def division():
  """
  divide N1 entre N2 y su total lo divide entre N3...
  y devuelve el resultado
  """
  global totalDivision
  global restoDivision
  NumerosCalculos = len(numeros2)
  totalDivision = numeros2[0] / numeros2[1]  # para poder calcular con ello le indicamos como debe operar
  restoDivision = numeros2[0] % numeros2[1]  
  for operacion in range(2,NumerosCalculos):
    totalDivision /= numeros2[operacion]
    restoDivision %= numeros2[operacion]
  return totalDivision, restoDivision
  

def multiplicacione():
  """
  multiplica N1 y N2 y su resultado por N3
  y devuelve el resultado
  """
  global totalMultiplicacion
  totalMultiplicacion = numeros2[0] #igualamos para poder calcular con ello
  NumeroCalculos = len(numeros2)
  for operacion in range(1,NumeroCalculos): #evitamos duplicar los calculos
    totalMultiplicacion *= numeros2[operacion]
  return totalMultiplicacion

#funciones de control

def pregunta_reinicio():
  global restart
  restart = input('Escribe "close" si quieres cerrar el programa o "continue" si quieres continuar: ')



"""
doble bucle 
primer bucle ejecuta el programa de manera infinita hasta que se llame a la funcion cerra
segundo bucle reinicia el prgrama si el usuario llama a reiniciar
"""
global programaBucleEjecucion
global programaBucle2
programaBucleEjecucion = True
programaBucle2 = True
while programaBucleEjecucion: 
  while programaBucle2:
    
    menu()
    decoracionMenu()
    menueleccion()
    decoracionMenu()


    if ValNum == 1:
      pedirNum()
      sumam()
      print(f'El resultado es: {totalsuma}')
      
    elif ValNum == 2:
      pedirNum()
      restar()
      print(f'El resultado es: {totalresta}')

    elif ValNum == 3:
      pedirNum()
      #cambiar por reinicio de los numeros
      division()
      print(f'El resultado es: {totalDivision} ', end='')
      print(f' y su resto es {restoDivision}')

    elif ValNum == 4:
      pedirNum()
      multiplicacione()
      print(f'El resultado es: {totalMultiplicacion}')
    print('Muchas gracias por confiar en mi tus calculos')
    decoracionMenu()
    pregunta_reinicio()
    if restart == 'close':
      programaBucle2 = False
      programaBucleEjecucion = False
    else:
      decoracionMenu()
      print('GENIAL!!!')



