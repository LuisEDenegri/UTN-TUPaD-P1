
#Trabajo Práctico Nº7: Recursividad
#Este módulo contiene todas las funciones pedidas y, al ejecutarse, permite probarlas de forma interactiva.


from __future__ import annotations

def factorial(n: int) -> int:
    #Calcula recursivamente el factorial de n (n!)
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    #Devuelve el valor de Fibonacci en la posición n (0‑indexado)
    if n < 0:
        raise ValueError("Índice negativo no permitido.")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def potencia(base: float, exponente: int) -> float:
    #Calcula base**exponente de forma recursiva
    if exponente < 0:
        return 1 / potencia(base, -exponente)
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


def decimal_a_binario(n: int) -> str:
    #Convierte un entero positivo a binario sin usar bin()
    if n < 0:
        raise ValueError("Solo acepta enteros positivos.")
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)


def es_palindromo(palabra: str) -> bool:
    #Verifica recursivamente si una palabra es palíndromo
    largo = len(palabra)
    if largo <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


def suma_digitos(n: int) -> int:
    #Suma los dígitos de un entero positivo sin convertirlo a string
    if n < 0:
        raise ValueError("Solo números positivos.")
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)


def contar_bloques(n: int) -> int:
    #Cuenta bloques para una pirámide de base n
    if n < 1:
        raise ValueError("n debe ser >= 1")
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


def contar_digito(numero: int, digito: int) -> int:
    #Cuenta cuántas veces aparece 'digito' en 'numero'
    if not (0 <= digito <= 9):
        raise ValueError("El dígito debe estar entre 0 y 9.")
    if numero == 0:
        return 1 if digito == 0 else 0
    if numero < 10:
        return 1 if numero == digito else 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)


# Módulo de prueba interactiva
if __name__ == "__main__":
    print("---- Factorial ----")
    limite = int(input("Calcular factorial hasta: "))
    for i in range(1, limite + 1):
        print(f"{i}! = {factorial(i)}")

    print("\n---- Fibonacci ----")
    pos = int(input("Mostrar serie hasta la posición: "))
    serie = [fibonacci(i) for i in range(pos + 1)]
    print("Serie:", serie)

    print("\n---- Potencia ----")
    base = float(input("Base: "))
    exp = int(input("Exponente: "))
    print(f"{base}^{exp} =", potencia(base, exp))

    print("\n---- Decimal a Binario ----")
    num = int(input("Número decimal: "))
    print("Binario:", decimal_a_binario(num))

    print("\n---- Palíndromo ----")
    palabra_in = input("Palabra: ").lower()
    print("¿Es palíndromo?", es_palindromo(palabra_in))

    print("\n---- Suma de dígitos ----")
    n_in = int(input("Número: "))
    print("Suma dígitos:", suma_digitos(n_in))

    print("\n---- Contar bloques ----")
    niveles = int(input("Bloques en el nivel más bajo: "))
    print("Bloques totales:", contar_bloques(niveles))

    print("\n---- Contar dígitos ----")
    num_in = int(input("Número: "))
    dig_in = int(input("Dígito a contar (0-9): "))
    print("Cantidad:", contar_digito(num_in, dig_in))
