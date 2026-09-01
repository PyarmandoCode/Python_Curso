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
Ademas imprimir el nombre del obrero
"""
pago_hora = 25  #ingreso
nombre_obrero = input("Ingrese el nombre del obrero:")
horas_trabajadas =  int(input("Ingrese las horas que trabajo:"))  #ingreso
jornal = horas_trabajadas * pago_hora # calculo
print(f"El Jornal diario que recibira {nombre_obrero} es {jornal}") #salida


