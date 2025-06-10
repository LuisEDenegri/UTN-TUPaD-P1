numero = input("Ingrese un número entero: ")
invertido = ""
#se ingresa un numero y se declara invertido
for digito in numero:
    invertido = digito + invertido
    #se guada el numero en forma de texto para poder imnvertirlo
print("El número invertido es:", invertido)
