num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

#Se ingresan ambos numero y se verifica cual de los dos es el mas grande

if num1 > num2:
    menor = num2
    mayor = num1
else:
    menor = num1
    mayor = num2

suma = 0
for i in range(menor + 1, mayor):
    suma = suma + i
#el for finalizara cuando llegue al numero mayor

print("La suma de los números enteros entre", menor, "y", mayor, "es:", suma)