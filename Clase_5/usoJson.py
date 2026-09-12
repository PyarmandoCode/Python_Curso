import json

alumnos = {
    "nombre":"Carlos",
    "curso":"Python",
    "nota":18,
}

with open("alumno.json","w") as archivo:
    json.dump(alumnos,archivo,indent=4)

print("Datos Guardados")    