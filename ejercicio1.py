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

# Datos de ventas por tienda (cada lista es una tienda, con ventas de julio a diciembre)
ventas = [
    [50000, 60000, 65000, 62000, 78000, 95000],  # ABSA 1
    [89000, 90000, 98000, 80000, 85000, 90000],  # ABSA 2
    [65000, 72000, 85000, 72000, 83000, 98000],  # ABSA 3
    [92000, 88000, 90000, 76000, 82000, 93000]   # ABSA 4
]

# Lista de nombres de tiendas
tiendas = ["ABSA 1", "ABSA 2", "ABSA 3", "ABSA 4"]

# a) Venta total de todas las tiendas
total_general = 0

# b) Venta total por tienda
totales = []
for tienda in ventas:
    total = sum(tienda)
    totales.append(total)
    total_general += total

# c) Tienda que más vendió
mayor_venta = max(totales)
tienda_mayor = tiendas[totales.index(mayor_venta)]

# d) Tienda que menos vendió
menor_venta = min(totales)
tienda_menor = tiendas[totales.index(menor_venta)]

# Mostrar resultados
print("a) Venta total de todas las tiendas:", total_general)
print("b) Venta total por tienda:")
for i in range(4):
    print(tiendas[i], ":", totales[i])
print("c) Tienda que más vendió:", tienda_mayor, "con", mayor_venta)
print("d) Tienda que menos vendió:", tienda_menor, "con", menor_venta)
