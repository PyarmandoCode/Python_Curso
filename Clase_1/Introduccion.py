"""
Una tienda quiere aplicar 20% de descuento 
cuando una compra supera los $/ 500.
1.-Pedir el Monto
2.-Verificar si supera los 500
3.-Calcular el descuento
4.-Mostrar cuanto debe pagar
"""
# Paso 1
#Tipos datos primitivos 
    #Numeros .- int (500) - float(520.20)
    #Cadena .- str('Hola Bienvenido al curso')
    #Logicos.- boolean(True/False) 
cliente = input("Ingrese el nombre del cliente:")    
compra = float(input("Ingrese el monto de compra:"))
# Paso 2
if compra > 500:
    # Paso 3
    descuento = compra * 0.20
else:
    # Paso 3
    descuento = 0    
# Paso 4    
total = compra - descuento
print(f"Lo que debe pagar el cliente {cliente} es {total} y su descuento fue de {descuento}")
