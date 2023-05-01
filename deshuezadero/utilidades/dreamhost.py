import os
import shutil
from home.models import *
from django.conf import settings
from pathlib import Path
from datetime import datetime, date, timedelta

RUTA = settings.RUTA
RUTA2 = settings.RUTA2

def moverArchivoProducto(file, id):
	if existeArchivoMedia(file)==True:
		fecha = datetime.now()
		nombre = f"{datetime.timestamp(fecha)}{os.path.splitext(str(file))[1]}"
		shutil.move(f'{RUTA}ejemplo_1/media/{file}', f'{RUTA2}assets/upload/producto/{nombre}')
		Producto.objects.filter(pk=id).update(foto=nombre)

def moverArchivoProducto3(file, id):
    #if existeArchivoMedia(file)==True:
    fecha = datetime.now()
    nombre = f"{datetime.timestamp(fecha)}{os.path.splitext(str(file))[1]}"
    shutil.move(f'{RUTA}ejemplo_1/media/{file}', f'{RUTA2}assets/upload/producto/{nombre}')
    Producto.objects.filter(pk=id).update(foto=nombre)


def moverArchivoProducto2(file):
    shutil.move(f'{RUTA}ejemplo_1/media/producto/{file}', f'{RUTA2}assets/upload/producto/{file}')


def existeArchivo(carpeta, archivo):
    try:
        ruta=f"{RUTA}ejemplo_1/assets/upload/{carpeta}/{archivo}"
        fileObj = Path(ruta)
        return fileObj.is_file()
    except Exception as e:
        return False


def existeArchivoMedia(archivo):
    try:
        ruta=f"{RUTA}ejemplo_1/media/{archivo}"
        fileObj = Path(ruta)
        return fileObj.is_file()
    except Exception as e:
        return False