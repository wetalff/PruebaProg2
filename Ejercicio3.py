#3. La linealización es un proceso por el cual, se transforma un arreglo bidimensional en un
#arreglo unidimensional. Existen tres técnicas para realizar este proceso: por filas, por
#columnas o en zigzag. Crear un programa que permita la linealización de un arreglo
#bidimensional por columnas. Los datos del arreglo bidimensional serán tomados de la tabla. 

# Creamos una matriz 3x3 con valores fijos (puedes cambiarla si quieres)
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Creamos la lista para almacenar la matriz linealizada por columnas
linealizada = []

# Recorremos por columnas primero
for columna in range(len(matriz[0])):  # len(matriz[0]) da el número de columnas
    for fila in range(len(matriz)):   # len(matriz) da el número de filas
        linealizada.append(matriz[fila][columna])

# Mostramos la lista linealizada por columnas
print("\nMatriz linealizada por columnas:")
print(linealizada)
