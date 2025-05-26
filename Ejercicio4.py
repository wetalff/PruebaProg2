# Pedimos la cantidad de filas y columnas (de 1 a 9)
while True:
    total_filas = int(input("¿Cuántas filas? (máx. 9): "))
    total_columnas = int(input("¿Cuántas columnas? (máx. 9): "))
    if 1 <= total_filas <= 9 and 1 <= total_columnas <= 9:
        break  # Si son válidas, salimos del ciclo

# Creamos la matriz pidiendo al usuario los valores
matriz = []
for f in range(total_filas):
    fila = []
    for c in range(total_columnas):
        valor = int(input(f"Valor en [{f+1},{c+1}]: "))
        fila.append(valor)
    matriz.append(fila)

# Mostramos la suma de cada fila
print("\nSuma de cada fila:")
for fila in matriz:
    print(sum(fila))

# Mostramos el promedio de cada columna
print("\nPromedio de cada columna:")
for c in range(total_columnas):
    suma = 0
    for f in range(total_filas):
        suma += matriz[f][c]
    print(round(suma / total_filas, 2))

# Buscamos el valor mayor y su posición
mayor = matriz[0][0]
pos_f, pos_c = 0, 0
for f in range(total_filas):
    for c in range(total_columnas):
        if matriz[f][c] > mayor:
            mayor = matriz[f][c]
            pos_f, pos_c = f, c

print(f"\nEl valor mayor es {mayor} y está en la fila {pos_f+1}, columna {pos_c+1}.")
