precios = [1200,1500,1900,2000,2200] #Lista

total = 0 #Variable Inicializar
for precio in precios:
    total += precio
    
promedio = total / len(precios)

print(f"El precio total de mis productos es {total}")
print(f"El promedio total de mis productos es {promedio}")

lista=[]
productos = input("Ingrese los Productos:")
lista.append(productos)