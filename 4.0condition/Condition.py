"""
Sentencias condicionales
Hecho por steve
07/12/2022
14:00 pm

"""


tipoSerVivo = input('¿El tipo de ser vivo en el que piensas esta dentro una planta o un animal? ') #Entrada tipo de ser vivo
if tipoSerVivo == 'si':
    serVivo = input('¿Es un animal o una planta?')
    if serVivo == 'animal': #Condicion para animal o planta
        patas = input('tiene patas?') #si es animal tiene patas o no
        if patas == 'si':
            strNumPatas = input('¿Cuantas patas tiene?')
            try: #captura excepcion para numero de patas invalido
                NumPatas = int(strNumPatas)
                if NumPatas == 0: #numero 0
                    print('si es 0 no tiene patas')
                elif NumPatas <= 2: # dos patas
                    print('Entonces es pajaro')
                elif  2 < NumPatas: # cuatro patas
                    print('Entonces va a cuatro patas')
                    peludo = input('¿Tiene pelo?') #condicion animal con patas 
                    if peludo == 'si':
                        print('Debe de ser un perro')
                    else:
                        print('Debe de ser un cocodrilo')
            except:
                print('Debes poner un valor numerico')
        else:
            print('De de ser un Gusano')
    elif serVivo == 'planta': # Condicion planta
        print('Entonces debe de ser una planta')
        planta = input('Tiene Tronco?')
        if planta == 'si': #Si tiene tronco
            print('Es un arbol!!')
        else:
            print('Es un Geranio')
else:
    print('Entonces no lo conozco')
        
    

