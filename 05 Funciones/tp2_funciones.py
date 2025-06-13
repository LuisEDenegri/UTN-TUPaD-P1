import math


def imprimir_hola_mundo() -> None:
   #Imprime 'Hola Mundo!' en pantalla.
    print("Hola Mundo!")


def saludar_usuario(nombre: str) -> str:
    
    #Devuelve un saludo personalizado.
    return f"Hola {nombre}!"


def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> None:
    #Imprime la información personal formateada.
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def calcular_area_circulo(radio: float) -> float:
    #Devuelve el área de un círculo dado su radio
    return math.pi * radio ** 2


def calcular_perimetro_circulo(radio: float) -> float:
    #Devuelve el perímetro de un círculo dado su radio
    return 2 * math.pi * radio


def segundos_a_horas(segundos: int) -> float:
    #Convierte segundos a horas (puede incluir decimales)
    return segundos / 3600


def tabla_multiplicar(numero: int) -> None:
    #Imprime la tabla de multiplicar del 1 al 10 para el número dado
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def operaciones_basicas(a: float, b: float) -> tuple[float, float, float, float | None]:
    #Devuelve una tupla con suma, resta, multiplicación y división (si b ≠ 0)
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return suma, resta, multiplicacion, division


def calcular_imc(peso: float, altura: float) -> float:
    #Calcula el índice de masa corporal (IMC)
    return peso / (altura ** 2)


def celsius_a_fahrenheit(celsius: float) -> float:
    #Convierte grados Celsius a Fahrenheit
    return celsius * 9 / 5 + 32


def calcular_promedio(a: float, b: float, c: float) -> float:
    #Devuelve el promedio de tres números
    return (a + b + c) / 3



# Ejecución interactiva
if __name__ == "__main__":
    imprimir_hola_mundo()

    nombre_in = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre_in))

    apellido_in = input("Ingrese su apellido: ")
    edad_in = int(input("Ingrese su edad: "))
    residencia_in = input("Ingrese su lugar de residencia: ")
    informacion_personal(nombre_in, apellido_in, edad_in, residencia_in)

    radio_in = float(input("Ingrese el radio de un círculo: "))
    print(f"Área: {calcular_area_circulo(radio_in):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio_in):.2f}")

    segundos_in = int(input("Ingrese la cantidad de segundos: "))
    print(f"Equivalen a {segundos_a_horas(segundos_in):.2f} horas")

    numero_in = int(input("Ingrese un número para su tabla de multiplicar: "))
    tabla_multiplicar(numero_in)

    a_in = float(input("Ingrese el primer número para operaciones básicas: "))
    b_in = float(input("Ingrese el segundo número: "))
    suma, resta, mult, div = operaciones_basicas(a_in, b_in)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")

    peso_in = float(input("Ingrese su peso en kg: "))
    altura_in = float(input("Ingrese su altura en metros: "))
    print(f"IMC: {calcular_imc(peso_in, altura_in):.2f}")

    celsius_in = float(input("Ingrese la temperatura en °C: "))
    print(f"{celsius_in} °C equivalen a {celsius_a_fahrenheit(celsius_in):.2f} °F")

    n1 = float(input("Ingrese el primer número para promedio: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    print(f"Promedio: {calcular_promedio(n1, n2, n3):.2f}")
