"""
Estructura de datos
* Lista [] .- Ordenada,Modificable,Duplicados
* Tupla () .- Ordenada,No,Duplicados
* Diccionarios {clave:valor} .-Si*,Modifable,Claves no
* Set {} .-No , Modificable,No Duplicados
"""
#Listas .- permite almacenar varios elementos en una sola
#Variable

frutas = ["Manzana","Pera","Naranja","Platano","Arandano"]

#Acceder a elementos por su posicion   
#print(frutas[4])
#Acceder mediante posiciones negativas
#print(frutas[-1])
#Modificar un elemento 
#frutas[1]="Fresa"
#Agregar elementos a una Lista
frutas.append("Uva")
frutas.insert(0,"Sandia")
#Eliminar elementos de una lista
#frutas.clear() #Eliminas todos
#frutas.pop(0)
#ordenar una  lista
frutas.sort()
#recorrer una lista
for fruta in frutas:
    print(fruta)
#print(frutas)
