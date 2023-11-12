import os


def fileWordCounter(nombre_fichero):
    file = open(nombre_fichero, "rt", encoding="utf8")
    numero_lineas = 0
    numero_palabras = 0
    numero_caracteres = 0
    for lineaRaw in file:
        linea = lineaRaw.strip('\n') # no contaremos el fin de línea como caracter

        palabras = linea.split() # Lista de palabras
        numero_lineas += 1
        numero_palabras += len(palabras)
        numero_caracteres += len(linea)
        
    file.close()
    return numero_lineas, numero_palabras, numero_caracteres


ficheros = os.listdir()
if 'Lista.txt' in ficheros:
    os.rename('Lista.txt', 'Lista(reescrita).txt')
    f = open('Lista_sobreescrita.txt', 'wt', encoding='utf8')
else:
    f = open('Lista.txt','wt', encoding='utf8')
f.write('Fichero;líneas;palabras;caracteres:' + '\n')
for fichero in  ficheros :
    try:
        if fichero.endswith('.py'):
            nLineas,nPalabras,nCaracteres = fileWordCounter(fichero)
            f.write('"{}";{};{};{};'.format(fichero,nLineas,nPalabras,nCaracteres) + '\n')
    except:
        pass
f.close()
        # print('Error con ',fichero)



