import tkinter as tk
from tkinter import ttk
import random
import os
class Aplicacion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #etiqueta numero de caracteres
        self.etiqueta_caracteres = ttk.Label(parent, text='Nº de caracteres:')
        self.etiqueta_caracteres.place(x=180, y=20)
        #caja de entrada
        self.caja_caracteres = ttk.Entry(parent)
        self.caja_caracteres.place(x=280, y=20, width=60)
        #sitio Web
        self.etiqueta_sitio = ttk.Label(parent, text='Sitio Web:')
        self.etiqueta_sitio.place(x=20, y=20, width=60)
        #caja sitio Web
        self.caja_sitio = ttk.Entry(parent)
        self.caja_sitio.place(x=80, y=20, width=60)

        #boton generar
        self.boton_Generar = ttk.Button(parent, text='Generar', command=self.generar_temp)
        self.boton_Generar.place(x=20, y=60)
        
        #Resultados
        self.etiqueta_temp_passwd = ttk.Label(parent, text='Contraseña es:')
        self.etiqueta_temp_passwd.place(x=20, y=120)
        self.etiqueta_temp_sitio = ttk.Label(parent, text='Contraseña para: ')
        self.etiqueta_temp_sitio.place(x=20, y=160)

        #guardar contraseña
        self.boton_Guardar = ttk.Button(parent, text='Guardar', command=self.Save_temp)
        self.boton_Guardar.place(x=20, y=200)


    def generar_temp(self):
        """
        Genera una contraseña aleatoria con distintos caracteres dentro de el codificado UTF8
        guarda la contraseña en temp_passwd
        guarda el sitio web en temp_sitio
        de manera global para que se pueda usar en su funcion adherida
        """
        global temp_sitio
        temp_sitio = self.caja_sitio.get()
        global temp_passwd
        temp_passwd = ''
        temp_longitud = int(self.caja_caracteres.get())
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,-:;<>][=-_+0123456789'
        for i in range(temp_longitud):
            temp_passwd = temp_passwd + random.choice(chars)
            
        self.etiqueta_temp_passwd.config(
            text=f'Contraseña es: {temp_passwd}')
        self.etiqueta_temp_sitio.config(
            text=f'Contraseña para: {temp_sitio}')
    def Save_temp(self):
        """
        Guarda las contraseñas con el sitio web
        sitioWeb = ''
        passwd = ''
        """
        listaficheros = os.listdir()
        if 'passwd.txt' in listaficheros:
            f = open('passwd.txt', 'a+', encoding='utf8')
            f.write('\n'+'----------------------------------'+'\n')
            f.write(f'password = {temp_passwd}' + '\n')
            f.write(f'Website = {temp_sitio}')
            f.close()

        else:
            f = open('passwd.txt','wt', encoding='utf8')
            f.write(f'password = {temp_passwd}' + '\n')
            f.write(f'Website = {temp_sitio}')
            f.close()

ventana = tk.Tk()
ventana.title('Generador de Contraseñas aleatorias')
ventana.config(width=400, height=300)
app = Aplicacion(ventana)
ventana.mainloop()