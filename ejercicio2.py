"""2. Se desea realizar un programa en donde se capture el nombre y tres calificaciones para
5 estudiantes de la facultad de Ingeniería, y después se pueda procesar dándonos el
promedio final de cada uno de los alumnos, el resultado se mostrará en pantalla."""

# Creamos una lista vacía para guardar los datos de los alumnos
estudiantes = []

# Capturamos los datos de 5 alumnos
for i in range(5):
    print(f"\nAlumno {i + 1}")
    nombre = input("Ingrese el nombre del alumno: ")
    
    # Capturamos tres calificaciones y las convertimos a float
    calificaciones = []
    for j in range(1, 4):
        calificacion = float(input(f"Ingrese calificación {j}: "))
        calificaciones.append(calificacion)
    
    # Guardamos el nombre y las calificaciones como una tupla o lista dentro de estudiantes
    estudiantes.append((nombre, calificaciones))

# Mostramos los promedios
print("\n--- Promedios Finales ---")
for nombre, calificaciones in estudiantes:
    promedio = sum(calificaciones) / 3  # Calculamos el promedio de 3 calificaciones
    print(f"{nombre}: {promedio:.2f}")