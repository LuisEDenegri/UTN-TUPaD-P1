pares = 0
impares = 0
negativos = 0
positivos = 0
#se inicializan las variables en 0

cantidad = 100  

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if numero < 0:
        negativos = negativos + 1
    elif numero > 0:
        positivos = positivos + 1
#se utiliza % para saber si es par, sino va ser impart y despues se verifica que sea positivo o negativo

print("Pares:", pares)
print("Impares:", impares)
print("Negativos:", negativos)
print("Positivos:", positivos)

#Se imprime por pantalla los resultados