"""1. La Abarrotera ABSA tiene 4 sucursales en las cuales se realizaron diferentes ventas en los
meses de Julio a diciembre del año 2022, se le ha solicitado a usted realizar un programa en
donde pueda capturar la siguiente tabla de datos:
Estado de cuenta de las Sucursales ABSA en el segundo semestre 2022
Tienda/Mes Julio Agosto Septiembre Octubre Noviembre Diciembre
________________________________________________________
|ABSA 1| 50,000| 60,000| 65,000| 62,000| 78,000| 95,000|
|ABSA 2| 89,000| 90,000| 98,000| 80,000| 85,000| 90,000|
|ABSA 3| 65,000| 72,000| 85,000| 72,000| 83,000| 98,000|
|ABSA 4| 92,000| 88,000| 90,000| 76,000| 82,000| 93,000|
________________________________________________________

y nos presente los siguientes resultados:
a. Venta total por todas las tiendas
b. Venta total por tienda
c. Tienda que más vendió en los 6 meses
d. Tienda que menos vendió"""

# Creamos una lista bidimensional: cada fila representa una tienda y cada columna un mes
ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],  # ABSA 1
    [89000, 90000, 98000, 80000, 85000, 90000],  # ABSA 2
    [65000, 72000, 85000, 72000, 83000, 98000],  # ABSA 3
    [92000, 88000, 90000, 76000, 82000, 93000]   # ABSA 4
]

# Nombres de las tiendas y los meses
tiendas = ['ABSA 1', 'ABSA 2', 'ABSA 3', 'ABSA 4']
meses = ['Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

print("Estado de cuenta de las Sucursales ABSA en el segundo semestre 2022")
print("-" * 88)  
print(f"{'Tienda/Mes':<10} | " + " | ".join([f"{mes:<10}" for mes in meses]))
print("-" * 88)

ventas_por_tienda = []  # Lista para guardar la suma total de cada tienda

# Recorremos cada tienda y sus ventas mensuales
for i, fila in enumerate(ventas): # Enumerate: Convierte una lista en algo que recorre y te da dos cosas a la vez
    ventas_por_tienda.append(sum(fila))  # Calculamos y guardamos la venta total por tienda
    print(f"{tiendas[i]:<10} | " + " | ".join([f"${v:<9,}" for v in fila]))
print("-" * 88)

# Sumamos todas las ventas de todas las tiendas para obtener el total general
venta_total = sum(ventas_por_tienda)

# Usamos funciones integradas para obtener la tienda con mayor y menor venta
max_tienda = tiendas[ventas_por_tienda.index(max(ventas_por_tienda))]  # Tienda con más ventas
min_tienda = tiendas[ventas_por_tienda.index(min(ventas_por_tienda))]  # Tienda con menos ventas

# Mostramos los resultados requeridos
print(f"\na) Venta total por todas las tiendas: ${venta_total:,}")
print("b) Venta total por tienda:")
for i, total in enumerate(ventas_por_tienda):
    print(f"{tiendas[i]}: ${total:,}")
print(f"c) Tienda que más vendió: {max_tienda} con ${max(ventas_por_tienda):,}")
print(f"d) Tienda que menos vendió: {min_tienda} con ${min(ventas_por_tienda):,}")