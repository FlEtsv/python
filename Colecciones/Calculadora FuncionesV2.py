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
  eleccion entre las distintas opciones dentro del programa
  solo numeros.
  """
  global ValNum
  ValNum = 0
  eleccion = dict[str:int]
  eleccion = {'suma':1, 'resta':2, 'multiplicacion':3, 'division':4}
  eleccionDef = input('¿Que operacion quieres hacer?')
  if eleccionDef in eleccion:
    for clave, valor in eleccion.items():
      if clave == eleccionDef:
        ValNum += valor
        
  else:
    print('No entiendo lo que me quieres decir :(')

#funciones Numericas

def pedirNum():
    condiNum = 'true'
    while(condiNum=='true'):
        global np1str
        global np2str
        np1str = input('Dime un numero: ')
        np2str = input('Dime un segundo numero: ')
        np1contador = len(np1str)
        np2contador = len(np2str)
        if np1contador > 0 and np2contador > 0:
            break
    
    global np1
    global np2
    np1 = int(np1str)
    np2 = int(np2str)
    return np1, np2
    
    

def suma(n1, n2):
  """
  suma n1 y n2
  devuelve resultado
  """
  global totalsuma
  totalsuma = n1 + n2
  return totalsuma
  

def resta(n1, n2):
  """
  resta n1 y n2
    devuelve el resultado
  """
  global totalresta
  totalresta = n1 - n2
  return totalresta
  

def division(n1, n2):
  global totalDivision
  global restoDivision
  totalDivision = n1 / n2
  restoDivision = n1 % n2
  return totalDivision, restoDivision
  

def multiplicacion(n1, n2):
  global totalMultiplicacion
  totalMultiplicacion = n1 * n2
  return totalMultiplicacion

#funciones de control

def pregunta_reinicio():
  global restart
  restart = input('Toca "r" si quieres cerrar el programa o "c" si quieres continuar: ')



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

    if ValNum == 1:
      pedirNum()
      suma(n1=np1, n2=np2)
      print(f'El resultado es: {totalsuma}')
      
    elif ValNum == 2:
      pedirNum()
      resta(n1=np1, n2=np2)
      print(f'El resultado es: {totalresta}')

    elif ValNum == 3:
      pedirNum()
      #cambiar por reinicio de los numeros
      division(n1=np1, n2=np2)
      print(f'El resultado es: {totalDivision} ', end='')
      print(f' y su resto es {restoDivision}')

    elif ValNum == 4:
      pedirNum()
      multiplicacion(n1=np1, n2=np2)
      print(f'El resultado es: {totalMultiplicacion}')
    print('Muchas gracias por confiar en mi tus calculos')
    decoracionMenu()
    pregunta_reinicio()
    if restart == 'r':
      programaBucle2 = False
      programaBucleEjecucion = False



