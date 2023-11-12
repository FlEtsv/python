import os

lista = os.listdir()
f = open('prueba_fichero.txt', 'wt')
for ficheros in os.listdir():
    ficheros
    f.write(f'{ficheros}' + '\n')