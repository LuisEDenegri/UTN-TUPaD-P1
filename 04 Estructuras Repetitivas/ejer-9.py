suma = 0

cantidad = 100

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    suma = suma + numero
    #una vez finalizado el ingreso de los 100 numeros y almacenados en suma 
media = suma / cantidad
#se calcula el promedio

print("La media de los", cantidad, "números es:", media)
