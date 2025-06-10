numero = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(1, numero + 1):
    suma += i
    #se acumula la suma en SUMA con el indice que va creciendo hasta llegar al numero, incluido este mismo
print("La suma de los números entre 0 y", numero, "es:", suma)
