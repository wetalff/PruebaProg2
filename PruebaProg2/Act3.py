#3. La linealización es un proceso por el cual, se transforma un arreglo bidimensional en un
#arreglo unidimensional. Existen tres técnicas para realizar este proceso: por filas, por
#columnas o en zigzag. Crear un programa que permita la linealización de un arreglo
#bidimensional por columnas. Los datos del arreglo bidimensional serán tomados de la tabla.


Matriz = [[10, 50, 40], 
         [30, 20, 60], 
         [70, 80, 90]]

print("-" * 22)
for fila in Matriz:
    for columna in fila:
        print(f"|{columna:> 5}", end = " ")
    print("|")
    print("-"*22)
    
print("Matriz Alineada por columnas")

print("-" * 36)
resultado = [Matriz[fila][col] for col in range(len(Matriz[0])) for fila in range(len(Matriz))]
print(resultado)
print("-" * 36)