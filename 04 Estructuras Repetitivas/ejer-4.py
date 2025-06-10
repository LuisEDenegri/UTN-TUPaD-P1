total = 0

numero = int(input("Ingrese un número entero (0 para terminar): "))

#Hasta que no se ingrese un 0, se ejecutara el while
while numero != 0:
    total = total + numero
    #se suma el numero al total
    numero = int(input("Ingrese otro número entero (0 para terminar): "))
    #se repite el enunciado al final del while para saber si termina el bucle
print("La suma total es:", total)