"""EXCEPCIONES
- VALIDAR
- CONTROLAR
- MANEJAR
- INFORMAR
- LIBERAR

- EXCEPCIONES FRECUENTES

| Excepción     | ¿Cuándo ocurre? | Ejemplo |
| `ValueError`  | El valor no es adecuado para una operación. | `int("hola")` |
| `TypeError`   | Se utiliza un tipo de dato incompatible. | `"10" + 5` |
| `ZeroDivisionError` | Se divide entre cero. | `10 / 0` |
| `IndexError`  | Se accede a una posición inexistente. | `[10, 20][5]` |
| `KeyError`    | Se busca una clave inexistente. | `{"nombre": "Ana"}["edad"]` |
| `FileNotFoundError` | El archivo solicitado no existe. | `open("no_existe.txt")` |
| `NameError`   | Se utiliza un nombre no definido. | `print(variable_inexistente)` |
| `AttributeError` | El objeto no tiene el atributo o método solicitado. | `"hola".append("a")` |

"""
# try:
#   #codigo que puede generar una excepcion
#   pass
# except ValueError as error:
#     #Se ejecuta si ocurre un value error
#     pass
# except ZeroDivisionError as error:
#     #Se ejecuta si ocurre zerodivisionerror
#     pass
# else:
#     #Se ejecuta si el bloque try termina sin excepciones
#     pass
# #raise:
# finally:
#     #Se ejecuta al salir de la estructura
#     #haya ocurrido una excepcion o no
#     pass

# try:
#     edad = int(input("Ingrese su edad:"))
#     print(f"Su edad es {edad}")
# except ValueError:
#     print("Error: debe ingresar un numero entero")
        
# try:
#     numero = float(input("Ingrese un numero:"))    
#     divisior= float(input("Ingrese el divisior:"))
#     resultado = numero/divisior
#     print(f"Resultado {round(resultado,2)}")
# except ZeroDivisionError:
#     print("Error: no se puede dividir entre cero")    
# except ValueError:
#     print("Error: debe ingresar datos numericos")    
try:
    numero = int(input("Ingrese un número entero: "))
    resultado = 100 / numero
    print(f"Resultado {resultado}")
except (ValueError,ZeroDivisionError)as error:
    print("No se pudo realizar la operacion")
    print(f"Detalle {error}")
else:
    print("No se encontro ningun error en el codigo")   
finally:
    print("La Operacion ha finalizado y se cerro los archivos")     
    
    
    
    


