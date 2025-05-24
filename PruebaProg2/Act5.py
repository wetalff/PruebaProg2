#5. Escriba el programa que tenga un arreglo bidimensional que almacena la cantidad de
#computadores vendidos por tres vendedores en cuatro zonas diferentes. Se pide mostrar:
#a. La zona en la que más computadores se vendió.
#b. El vendedor que menos computadores vendió.
#c. La cantidad de computadores vendidos por todos los vendedores en todas las zonas.

Vendedores = ["Vendedor 1" "| " "Vendedor 2" "| " "Vendedor 3|"]        #Creo una lista con los vendedores
zonas = [[7, 4, 5], 
         [9, 11, 3],                                                    #creo una matriz con las ventas de las zonas
         [2, 1, 12],
         [7, 8, 9]]                                

print("-" * 39)                                                             
print(Vendedores)   #Imprimo la lista de vendedores para que se junte correctamente con sus respectivas ventas en la matriz

print("-" * 39)
for fila in zonas:                              #Se imprime la matriz de zonas original sin cambios
    for columna in fila:
        print(f"|{columna:>10}", end = " ")
    print("|")
    print("-"*37)
    
                                                                           
fila_max = max(zonas, key=sum)                             #Aqui encontramos la fila con la mayor suma


indice = zonas.index(fila_max)               # Obtenemos también la posicion de esa filae en la matriz
suma = sum(fila_max)                         # obtenemos la suma total de la mayor fila                        

print(f"La zona en que mas computadoras se vendio fue en la zona numero {indice + 1} con un total de {suma} computadoras vendidas")



                                                             
suma_col1 = sum(fila[0] for fila in zonas)  #Sumamos cada uno de los valores de cada fila
suma_col2 = sum(fila[1] for fila in zonas)
suma_col3 = sum(fila[2] for fila in zonas)
                                                                 
sumas = [suma_col1, suma_col2, suma_col3]   #Las guardamos en una lista para despues buscar cual es la menor

                                                                      
menor = min(sumas)
indice = sumas.index(menor)                 #Buscamos cual es la menor junto a su posicion en la matriz

print(f"El vendedor que menos computadoras vendio fue el vendedor numero {indice + 1} con un total de {menor}")



   
    
Suma_total = 0
                                           
for fila in zonas:                      #Aqui sumamos todos los valores de todas las filas para calacular el total de 
    for valor in fila:                  #computadoras vendidas
        Suma_total += valor
print("La cantidad total de computadoras vendidas fue de:", Suma_total)

