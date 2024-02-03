# Código creado por Sebastián Sterling

#####################################################################################################

import pygame

running = False

#####################################################################################################


#####################################################################################################

def play_song1():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("assets/music/suspenso.mp3")
    pygame.mixer.music.play()

def play_song2():
    global running
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("assets/music/bosque.mp3")
    pygame.mixer.music.play()

    # Establecer el evento de finalización de la música
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

    # Bucle de eventos de pygame
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                # La canción ha terminado, reproducir nuevamente
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()

def play_song3():
    global running
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("assets/music/fart.mp3")
    pygame.mixer.music.play()

    # Establecer el evento de finalización de la música
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

    # Bucle de eventos de pygame
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                # La canción ha terminado, reproducir nuevamente
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()

#####################################################################################################


# Definir el diccionario con las canciones
switch = {
    1: play_song1,
    2: play_song2,
    3: play_song3
}

# Inicializar pygame y el módulo de audio
pygame.init()
pygame.mixer.init()

def stop_music():
    global running
    running = False

#####################################################################################################

# Función para seleccionar y reproducir la canción
def select_song(song):
    # Obtener la función correspondiente a la canción
    if song == 1:
        play_song1()   
    elif song == 2:
        play_song2()
    elif song == 3:
        play_song3()
    elif song == -1:
        stop_music()

#####################################################################################################

# Detener y finalizar pygame
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()