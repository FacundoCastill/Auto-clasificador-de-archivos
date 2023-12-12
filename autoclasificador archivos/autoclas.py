import os
import shutil

directorio_origen = 'C:/Users/Oh Yeah/Desktop/desorgani'

directorio_destino = 'C:/Users/Oh Yeah/Desktop/organi'

def organizar_archivos_por_extension(directorio_origen, directorio_destino):
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)

    for filename in os.listdir(directorio_origen):

        archivo_origen = os.path.join(directorio_origen, filename)

        if os.path.isfile(archivo_origen):
            _, extension = os.path.splitext(filename)
            extension = extension[1:]
            carpeta_destino = os.path.join(directorio_destino, extension)
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            archivo_destino = os.path.join(carpeta_destino, filename)
            shutil.move(archivo_origen, archivo_destino)
            print(f'Movido: {filename} a {carpeta_destino}')

organizar_archivos_por_extension(directorio_origen, directorio_destino)