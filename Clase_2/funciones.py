"""
Una función es un bloque de código que realiza una tarea 
específica y que podemos reutilizar varias veces

def nombre_funcion():
    #Instrucciones
"""

#crear una funcion que me permita sumar dos numeros
def sumar_numeros(num1,num2):
    resultado = num1 + num2
    return resultado

#crear una funcion que reciba una compra y calcule un descuento
#del 20%
def calcular_total(compra):
    descuento = compra*0.20
    total = compra - descuento
    return total

#Funcion que retorne mas de un valor
def operaciones (a,b):
    suma = a + b
    resta = a - b
    return suma , resta

def operacionesII(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    #division = a / b #Division decimal
    division = a // b # Division entera
    return suma , resta , multiplicacion , division

#crear una funcion que me permita calcular el sueldo de un obrero
def calcular_sueldo (nombre,sueldo):
    """
    Esta Funcion calcula el sueldo final de un empleado
    La Funcion Round me permite rendondear un valor numerico flotante
    La Funcio f me permite unir cadenas con variables {}
    """
    bono = sueldo * 0.30
    total = sueldo + bono
    return nombre , bono , total
empleado , bono ,sueldo_final = calcular_sueldo("Carlos",1740.872)
#print(f"Empleado: {empleado}")
#print(f"Bono {round(bono,2)}")
#print(f"Sueldo Final {round(sueldo_final,2)}")

#Crear una funcion con valores predeterminados
def saludar(nombre ="Invitado"):
    """
    Este funcion tiene un valor por defecto
    """
    return nombre

#print(saludar("Jose"))

def numeros (*args):
  """
  permite recibir una cantidad variable de argumentos
  python guarda esos argumentos en una tupla
  (12,56,78,90)
  """
  for numero in args:
      print(numero)
  

numeros(10,20,30,40,50,56,12,78,96,34,56,78)  
  

#res_suma,res_resta,res_mul,res_div = operacionesII(20,5)    
#print(res_suma)
#print(res_resta)
#print(res_mul)
#print(res_div)

#resultado = operaciones(20,5)
#print(resultado)

#print(calcular_total(1000))
#print(sumar_numeros(10,20))
#print(sumar_numeros(5,2))
#print(sumar_numeros(100,223))