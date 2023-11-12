"""
Ejercicios/Tema3
Programa creado por Steven
11;25
06/12/2022
"""

nombre = input('¿Cómo te llamas? ')
print(f'Hola {nombre}')
strEdad = input('¿Cuantos años tienes? ')
try:
    edad = int(strEdad) #captura de excepcion edad
    cadena = f'Tienes {edad} años y naciste en el año {2021 - edad}'
    print(cadena)
except:
    print('Introduce una Edad validad')
    
numeroPersona = input('¿Me das un numero? para hacer operaciones ')
try:
    numeroOperaciones = int(numeroPersona) #captura de excepcion numeros de las operaciones y conversion de numeroOperacones en int
    numeroOperarstr = input('¿Por cual numero quieres operar? ') #captura str numero Operacion
    numeroOperarint = int(numeroOperarstr) #conversion
    
except:
    print('Porfavor introduce un numero valido') 

cadenaInformacion = f'El numero que me has dado es {numeroOperaciones}, que se va a dividir, multiplicar, sumar y restar por {numeroOperarint}'
print(cadenaInformacion)
cadenaDivision = f'El resultado de la division {numeroOperaciones//numeroOperarint} su resto es {numeroOperaciones%numeroOperarint}'
print(cadenaDivision)
cadenaMultiSumaResta = f'El resultado de la multiplicacion {numeroOperaciones*numeroOperarint}, su Suma es {numeroOperaciones+numeroOperarint} y su resta es {numeroOperaciones-numeroOperarint}'
print(cadenaMultiSumaResta)
