"""
hecho por Steven
20:00
18/01/23
Tema 9 POO
"""
import os

class coche():
    def __init__(self, tipo, asientos, potencia, velocidad_Punta, peso):
        self.tipo = tipo
        self.asientos = asientos
        self.potencia = potencia
        self.velocidad_Punta = velocidad_Punta
        self.peso = peso


    def __str__(self):
        return  f"SEGMENTO \t\t {self.tipo}\n" \
                f"NÚMERO DE ASIENTOS\t\t {self.asientos}\n" \
                f"CABALLOS DE FUERZA\t {self.potencia}\n" \
                f"VELOCIDAD PUNTA\t\t {self.velocidad_Punta}\n" \
                f"PESO\t\t {self.peso}\n"


class coche_Electrico(coche):

    autonomia = ''
    tiempoCarga = ''

    def __str__(self):
        return  f"SEGMENTO \t\t {self.tipo}\n" \
                f"NÚMERO DE ASIENTOS\t\t {self.asientos}\n" \
                f"CABALLOS DE FUERZA\t {self.potencia}\n" \
                f"VELOCIDAD PUNTA\t\t {self.velocidad_Punta}\n" \
                f"PESO\t\t {self.peso}\n" \
                f"AUTONOMIA\t\t {self.autonomia}\n" \
                f"TIEMPO DE CARGA\t\t {self.tiempoCarga}\n"


class coche_Combustion(coche):
    autonomia = ''
    capacidad_l = ''
    consumo = '' 
    def __str__(self):
        return  f"SEGMENTO \t\t {self.tipo}\n" \
                f"NÚMERO DE ASIENTOS\t\t {self.asientos}\n" \
                f"CABALLOS DE FUERZA\t {self.potencia}\n" \
                f"VELOCIDAD PUNTA\t\t {self.velocidad_Punta}\n" \
                f"PESO\t\t {self.peso}\n" \
                f"AUTONOMIA\t\t {self.autonomia}\n" \
                f"CAPACIDAD (L)\t\t {self.capacidad_l}\n" \
                f"CONSUMO(L)\t\t {self.consumo}\n" 




class coche_hibrido(coche):
    autonomiaElectrica = ''
    autonomiaCombustible = ''
    TiempoCarga = ''

    def __str__(self):
        return  f"SEGMENTO \t\t {self.tipo}\n" \
                f"NÚMERO DE ASIENTOS\t\t {self.asientos}\n" \
                f"CABALLOS DE FUERZA\t {self.potencia}\n" \
                f"VELOCIDAD PUNTA\t\t {self.velocidad_Punta}\n" \
                f"PESO\t\t {self.peso}\n" \
                f"AUTONOMIA ELECTRICA\t\t {self.autonomiaElectrica}\n" \
                f"AUTONOMIA MOTOR COMBUSTION\t\t {self.autonomiaCombustible}\n" \
                f"TIEMPO DE CARGA\t\t {self.TiempoCarga}\n" 


Volvo_xc90 = coche_Electrico('SUV','7','209cv','220km/h','2200kg')
Volvo_xc90.tiempoCarga = '40min'
Volvo_xc90.autonomia = '600km'



Mercedez_Gls = coche_Combustion('SUV', '5', '200cv', '216km/h', '2046kg')
Mercedez_Gls.capacidad_l = '60L'
Mercedez_Gls.consumo = '9L/100km'
Mercedez_Gls.autonomia = '666km'



Toyota_CHR = coche_hibrido('SUV', '5', '200cv', '198km/h', '2000kg')
Toyota_CHR.autonomiaCombustible = '450km'
Toyota_CHR.autonomiaElectrica = '50km'
Toyota_CHR.TiempoCarga = '1h'


while True:
    cocheMarca = input('Dime la marca de coche: ')
    fMarcas = open('MARCAS.txt', 'rt', encoding='utf8')
    for lineas in fMarcas:
        if cocheMarca == lineas:
            print('ya esta esa mara registrada')
        else:
            Marca_archivo = cocheMarca.upper()
            fMarcas.write(f'{Marca_archivo}' + '\n')
            print('Marca registrada.')
        fMarcas.close()
    
    print('Rellena el formulario.')
    print('MARCA Y MODELO:')
    Coche_Intermediario = input('"NISSAN JUKE"')
    tipoP = input('SEGMENTO: ')
    asientosP = int(input('Nº ASIENTOS: '))
    potenciaP = int(input('POTENCIA (cv): '))
    velocidadPuntaP = int(input('VELOCIDAD PUNTA: '))
    pesoP = int(input('PESO (kg): '))

    Cond_Propulsion = input('¿Qué clase de coche es?')
    if Cond_Propulsion == 'electrico':
        Objeto = coche_Electrico(tipoP, asientosP, potenciaP, velocidadPuntaP, pesoP)
        Objeto.autonomia
        Objeto.tiempoCarga

    elif Cond_Propulsion == 'combustion':
    
    elif Cond_Propulsion == 'hibrido':

    else:


    




        
    




    
