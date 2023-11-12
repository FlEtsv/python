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
def menueleccion():
  """
  eleccion entre las distintas opciones dentro del programa
  solo numeros.
  """
  print('Pulsa 1 si lo que quieres es sumar')
  print('Pulsa 2 si lo que quieres es restar')
  print('Pulsa 3 si lo que quieres es Dividir')
  strEleccion = input('Pulsa 4 si lo que quieres es hacer una Multiplicación: ')             
  try:
    global eleccion
    eleccion = int(strEleccion)
  except:
     print('No entiendo lo que me quieres decir')



def pedirNum():#SEGUIR CON LA PETICION DE NUMERO
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
  
  
  
menu()
decoracionMenu()
menueleccion()

if eleccion == 1:
  pedirNum()
  suma(n1=np1, n2=np2)
  print(f'El resultado es: {totalsuma}')
  
elif eleccion == 2:
  pedirNum()
  resta(n1=np1, n2=np2)
  print(f'El resultado es: {totalresta}')

elif eleccion == 3:
  pedirNum()
  division(n1=np1, n2=np2)
  print(f'El resultado es: {totalDivision} ', end='')
  print(f' y su resto es {restoDivision}')

elif eleccion == 4:
  pedirNum()
  multiplicacion(n1=np1, n2=np2)
  print(f'El resultado es: {totalMultiplicacion}')
else:
  print('Aun no tenemos esa operacion disponible')
  
print('Muchas gracias por confiar en mi tus calculos')
decoracionMenu()