# Código creado por Sebastián Sterling

# El programa lee una serie de archivos de texto y coloca su información 
# en arreglos para posteriormente ejecutarlos en un loop para hacer la función de GIF

import os
import sys
import time

def leer_documento(nombre_archivo):
    lines = []  # Inicializar la variable lines
    # Verificar que se encuentre el archivo y se
    if os.path.isfile(nombre_archivo):

        with open(nombre_archivo, "r", encoding="utf-8") as file:
            lines = file.readlines()
            file.seek(0)
        file.close()

    # Imprimir el archivo
    for line in lines:
        print(line.rstrip())

# Se queda recorriendo para siempre
i = 1
while True:
    nombre_archivo = "b/" + str(i) + ".txt"
    leer_documento(nombre_archivo)
    time.sleep(0.01)

    i = (i % 67) + 1
    
    os.system("cls")  # Para Windows, usar "clear" en sistemas Unix

# Esta forma imprime lo que hay en lo documentos directamente
