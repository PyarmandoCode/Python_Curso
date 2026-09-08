#print("Bienvenidos al curso de Python")
#print("Hoy Aprenderemos los fundamentos")

num1 = 20 #int 
num2 = 18
num3 = 15.8 #float
nombre = 'Carlos' #str
activado = True #bool
sumar = num1 + num2 
restar = num1 - num2 
multiplicar = num1 * num2 
division = num1 // num2

"""
print("Suma es:",sumar)
print("Resta es:",restar)
print("Multiplicacion es:",multiplicar)
print("Division es:",division)
"""

"""
Hallar el Pago que recibira un obrero de acuerdo a 
Sus horas trabajadas , si el pago por hora es de 25
Ademas imprimir el nombre del obrero.
Por politicas de la empresa un obrero no puede trabajar mas de 6 horas
Diarias
"""
"""
pago_hora = 25  #ingreso
nombre_obrero = input("Ingrese el nombre del obrero:")
horas_trabajadas =  int(input("Ingrese las horas que trabajo:"))  #ingreso
if horas_trabajadas>6:#indentacion
    print("Por Politicas de la empresa no se puede trabajar mas de 6 horas")
else:    
    jornal = horas_trabajadas * pago_hora # calculo
    print(f"El Jornal diario que recibira {nombre_obrero} es {jornal}") #salida

"""
"""
edad = 20
if edad >=18:
    print("La Persona es mayor de edad")
else:
    print("La Persona es menor de edad")    
"""    

"""
los bucles permiten repetir instrucciones automatica
Los Principales en python son:
-for
-while
"""
for num in range(1,16):
    print(f"Hola Soy un bucle y estoy en la vuelta {num}")
