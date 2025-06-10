#Se le pide que ingrese el numero al usuario
numero = input("Ingrese un número entero: ")

contador = 0


for digito in numero:
    if digito.isdigit():
        contador = contador + 1


print("El número tiene", contador, "dígitos.")