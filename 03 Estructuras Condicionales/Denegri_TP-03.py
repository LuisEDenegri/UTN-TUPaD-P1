# ejercicio 1
edad = int(input("Ingresa tu edad: "))
if edad > 18:
    print("Sos mayor de edad")
  
# ejercicio 2
nota = float(input("Ingresa tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
  
# ejercicio 3
numero = int(input("Ingresa un numero: "))
if numero % 2 == 0:
    print("Tu numero es par")
else:
    print("Por favor, ingresa un numero par")
  
# ejercicio 4
edad = int(input("Ingresa tu edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
  
# ejercicio 5
contraseña = input("Ingresa tu contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Ingrese una contraseña de entre 8 y 14 caracteres")
  
#ejercicio 6
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Sesgo no claro")
  
# ejercicio 7
frase = input("Ingrese una horacion o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# ejercicio 8
nombre = input("Ingresa tu nombre: ")
opcion = input("Ingresa 1 para mayusculas, 2 para minusculas o 3 para primera letra mayuscla: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opcion invalida")

# ejercicio 9
magnitud = float(input("Ingresa la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy bajo (imperceptible)")
elif 3 <= magnitud < 4:
    print("Bajo (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras debiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# ejercicio 10
hemisferio = input("Ingresa un hemisferio (N/S): ").upper()
mes = int(input("Ingresa un mes (1-12): "))
dia = int(input("Ingresa un dia (1-31): "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    print("Estacion:", estacion_norte)
elif hemisferio == "S":
    print("Estacion:", estacion_sur)
else:
    print("Hemisferio invalido")


