"""
bucles (while)
10 Multiplos de 7


"""
srNumeroMultiplos = input('De que numero quieres sacar los multiplos?')
strMenorque = input('hasta que numero quieres saer el multiplo')
strNumeroReps = input('cuantos multiplos necesitas?')
numeroReps = int(strNumeroReps)
numeroMultiplos = int(srNumeroMultiplos)
menorque = int(strMenorque)

numeroRepsCont = 0
contador = 1
while contador <= menorque:
    if contador % numeroMultiplos == 0:
        print(contador)
        numeroRepsCont += 1
        if numeroRepsCont == numeroReps:
            print('Aqui tienes los multiplos')
            break
    contador += 1
else:
    print('No hay multiplos')
    
    
print('hemos terminado')

    