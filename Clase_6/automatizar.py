import os
import shutil

#Carpeta que queremos organizar

carpeta = r"C:\Python_Curso\ARCHIVOS"

#Categorias y extensiones

categorias = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "PDF": [".pdf"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Word": [".docx", ".doc"],
    "Videos": [".mp4", ".avi", ".mkv"]
}

#Recorre los archivos

for archivo in os.listdir(carpeta):
    ruta_archivo = os.path.join(carpeta,archivo)
    #Solo trabajar con archivos
    if os.path.isfile(ruta_archivo):
        #Obtener extension
        extension = os.path.splitext(archivo)[1].lower()
        encontrado=False
        #Buscar a que categoria pertenece
        for categoria,extensiones in categorias.items():
            if extension in extensiones:
                carpeta_destino = os.path.join(carpeta,categoria)
                #Crear carpeta si no existe
                os.makedirs(
                    carpeta_destino,exist_ok=True
                )
                #Mover Archivos
                shutil.move(
                    ruta_archivo,os.path.join(carpeta_destino,archivo)
                )
                print(f"{archivo} -> {categoria}")
                encontrado=True
                break
            #Si no pertenece a ninguna categoria
        if not encontrado:
            carpeta_otros = os.path.join(carpeta,"Otros")
            os.makedirs(carpeta_otros,exist_ok=True)
            shutil.move(ruta_archivo,os.path.join(carpeta_otros,archivo))
            print(f"{archivo}->Otros")
print("\n ORGANIZACION TERMINADA")                
        
    