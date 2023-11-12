"""
Generadoy keys en flask
"""

from flask import Flask, request
import random
app = Flask('Hello Flask')

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/test')
def test():
    return 'test Flask'


@app.route('/GeneradorKeys',methods = ["GET", "POST"])
@app.route('/GeneradorKeys/',methods = ["GET", "POST"])
def GeneradorKeys():
    htmlCode = ""
    if request.method == "POST":
        print("POST") # Obtenemos datos y calcula
        tamaño = int(request.form.get("tamaño"))
        sitioWeb = request.form.get("sitioWeb")
        temp_passwd = ''
        temp_longitud = int(tamaño)
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,-:;<>][=-_+0123456789@#%$'
        for i in range(temp_longitud):
            temp_passwd = temp_passwd + random.choice(chars)
        htmlCode = """<h1>GeneradorKeys</h1>"""f'su contraseña es: {temp_passwd}'"""<br/>""" + f'Y pertenece al sitio web: {sitioWeb}'
            
    else:
        print("GET") # Mostramos HTML
        htmlCode = '''<h1>GeneradorKeys</h1>
                <form action="/GeneradorKeys" method="POST">
                <label>Numero de digitos:</label>
                <input type="text" name="tamaño"/>
                <label>sitio Web:</label>
                <input type="text" name="sitioWeb"/><br/><br/>
                <input type="submit"/>
                </form>'''
    return htmlCode

if __name__ == '__main__':
    app.run(debug = False, host='127.0.0.1') # solo acceso local y puerto 5000