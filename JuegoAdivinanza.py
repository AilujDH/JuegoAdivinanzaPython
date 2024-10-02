
import random

numero_secreto= random.randint (0,100)
cant_intentos= 0
cant_max_intentos= 3
adivinado= False

print ("Bienvenidos al juego de adivinanza de un numero secreto")

while not adivinado:
    if cant_intentos>= cant_max_intentos:
         print ("Game over! Keep on trying!")
         break

    numero= int (input ("Introduce un numero del 1 al 99: "))

    if numero== numero_secreto:
        print ("Felicidades! Has adivinado!")
        advinado= True
    elif numero< numero_secreto:
        print ("El numero es mayor al ingresado")
    else:
        print ("El numero es menor al ingresado")
cant_intentos+=1





