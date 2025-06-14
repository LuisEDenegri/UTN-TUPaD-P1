#Trabajo Práctico Nº6: Estructuras de datos complejas (sin objetos)
#Incluye diccionarios, tuplas y sets con entrada y salida por consola.


# 1) Agregar frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})

# 2) Actualizar precios
precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})

# 3) Lista solo con frutas
solo_frutas = list(precios_frutas.keys())
print("Frutas:", solo_frutas)

# 4) Agenda telefónica
agenda = {}
for _ in range(5):
    nombre = input("Nombre del contacto: ")
    numero = input("Número telefónico: ")
    agenda[nombre] = numero

buscar = input("¿De quién desea saber el número?: ")
if buscar in agenda:
    print(f"{buscar}: {agenda[buscar]}")
else:
    print("Contacto no encontrado.")

# 5) Frase a palabras únicas y conteo
frase = input("Ingrese una frase: ")
palabras = frase.lower().split()
unicas = set(palabras)
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("Palabras únicas:", unicas)
print("Frecuencia:", conteo)

# 6) Notas y promedio por alumno
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese nota {i+1}: ")) for i in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} - Promedio: {promedio:.2f}")

# 7) Sets de aprobados
parcial1 = {101, 102, 103, 104}
parcial2 = {103, 104, 105}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Solo uno de los dos:", parcial1 ^ parcial2)
print("Al menos uno:", parcial1 | parcial2)

# 8) Gestión de stock
stock = {'arroz': 10, 'fideos': 5}
producto = input("Producto a consultar: ")
if producto in stock:
    cant = int(input("¿Cuántas unidades desea agregar?: "))
    stock[producto] += cant
else:
    nuevo = int(input("Producto nuevo. ¿Cuántas unidades desea agregar?: "))
    stock[producto] = nuevo
print("Stock actualizado:", stock)

# 9) Agenda de eventos con tuplas
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunión de equipo',
    ('Martes', '14:00'): 'Clase de programación',
}
dia = input("Día a consultar: ")
hora = input("Hora a consultar: ")
evento = agenda_eventos.get((dia, hora), "Sin actividad registrada")
print("Evento:", evento)

# 10) Invertir diccionario país-capital
paises = {'Argentina': 'Buenos Aires', 'Francia': 'París', 'Brasil': 'Brasilia'}
capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", capitales)
