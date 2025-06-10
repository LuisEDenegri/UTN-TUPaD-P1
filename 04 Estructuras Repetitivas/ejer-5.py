import random
#se importa random para obtener numeros aleatorios
numero_secreto = random.randint(0, 9) #entre 0 y 9
intentos = 0

adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (0 a 9): "))
    intentos = intentos + 1
    #se contabilizan los intentos antes de adivinar el resultado
    if intento == numero_secreto:
        adivinado = True
        #si acierta se finaliza el while

print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
