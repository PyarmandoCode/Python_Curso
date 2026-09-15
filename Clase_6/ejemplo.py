"""
AUTOMATIZAR archivos con Python
"""
import os # (Sistema Operativo) permite que python interactue con carpetas
#archivos y rutas d windows , Linux macos
import shutil #Operaciones mas completas con Archivos

archivos = os.listdir(r"C:\Python_Curso\ARCHIVOS")
print(archivos)

#Crear una carpeta
os.makedirs (r"C:\Python_Curso\ARCHIVOS\Imagenes",exist_ok=True)

#Mover un Archivo

shutil.move (
     r"C:\Python_Curso\ARCHIVOS\foto1.jpg",
     r"C:\Python_Curso\ARCHIVOS\Imagenes\foto1.jpg",
)