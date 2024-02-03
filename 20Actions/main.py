# Código creado por Sebastián Sterling

#####################################################################################################

import os
import time
import threading
import pygame
import sys

from mixer import select_song
from mixer import stop_music
from decisions import select_decision

#####################################################################################################

stop = False  # Variable para controlar el ciclo principal
exit = False

#####################################################################################################


#####################################################################################################
# Limpiar pantalla
def clear():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Unix/Linux/Mac
        os.system("clear")

#####################################################################################################


#####################################################################################################

def read_input():
    global stop
    global exit
    while not stop:
        key = input()
        if key == '':
            stop = True
            stop_music()
        if key == "x":
            stop = True
            exit = True

#####################################################################################################


#####################################################################################################

def main():
    global stop
    global exit
    # Ruta de los archivos
    titulo = "assets/escenarios/Portada.txt"  
    titulo1 = "assets/escenarios/Portada1.txt"
	
    if os.path.isfile(titulo):
        with open(titulo, "r", encoding="utf-8") as file:
            lines = file.readlines()
            file.seek(0)
    if os.path.isfile(titulo1):
        with open(titulo1, "r", encoding="utf-8") as files:
            liness = files.readlines()
            files.seek(0)

    # Iniciar el hilo para reproducir música
    music_thread = threading.Thread(target=select_song, args=(1,))
    music_thread.start()

    # Iniciar el hilo para leer la entrada de teclado
    input_thread = threading.Thread(target=read_input)
    input_thread.start()

    while not stop:
        # Ciclo para dibujar y limpiar la pantalla
	
        # Dibujar
        for line in lines:
            print(line.rstrip())  # Imprime cada línea del archivo
        
        time.sleep(1)  # Esperar 1 segundo

        # Limpiar pantalla
        clear()

        for line in liness:
            print(line.rstrip())  # Imprime cada línea del archivo

        time.sleep(1)  # Esperar 1 segundo

        # Limpiar pantalla
        clear()

    # Cerrar los archivos
    if os.path.isfile(titulo):
        file.close()
    if os.path.isfile(titulo1):
        files.close()

    # Detener la música
    pygame.mixer.music.stop()

    # Esperar a que los hilos terminen
    music_thread.join()
    input_thread.join()

    #  Que empiece el juego
    if exit != True:
        juego()
    else:
        sys.exit()

#####################################################################################################


#####################################################################################################

def juego():

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t _________")
    print("\t\t\t\t| Iniciar |")
    print("\t\t\t\t|_________|")
    print("\n\n\n___________________________________________________________________________________")
    a = "Iniciar"
    b = "Esperar"
    select_decision(a, b)

#####################################################################################################


main()