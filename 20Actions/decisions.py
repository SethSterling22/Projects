# Código creado por Sebastián Sterling

#####################################################################################################

import os
import time
import threading

from mixer import select_song
from mixer import stop_music

#####################################################################################################

class TreeNode:
    def __init__(self, text, option1, option2, action):
        self.text = text
        self.option1 = option1
        self.option2 = option2
        self.action = action

        self.left = None
        self.right = None

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

# Crear los nodos del árbol con texto asociado
root = TreeNode("Despiertas, sientes una estrechez entre tus hombros, sientes incomodidad.\nVes una luz...", "Volver a la oscuridad", "Caminar hacia ella", 0)
root.left = TreeNode("Recuerdas el tiempo cuando vivías, pero…\n¿Por qué volver a la vida?", "No quiero volver...", "Ponerse de pie", 0)
root.right = TreeNode("Te desvaneces con la luz", "Qué es esto?", "El desarrollador no tuvo más tiempo?", 0)
# root.left.left = TreeNode("Texto del nodo izquierdo izquierdo", "a", "b")
root.left.right = TreeNode("Ves a tu alrededor y aparece ante tus ojos la figura de distintos esqueletos.\nPor alguna extraña razón te sientes parte de ellos", "Esperar", "Seguirlos", 4)
root.left.right.right = TreeNode("Los sigues  a paso lento hasta llegar a una caverna donde los caminantes\nesqueletos reposan y se desmoronan", "Seguir el camino", "Dar la vuelta", 0)
root.left.right.right.left = TreeNode("Te encuentras con un Gatito blanco con manchas negras\n- Su piel es impecable ha pasado a nueva vida recientemente (piensas)\nEl gato lleva un papel en la boca y te lo da", "Tomarlo", "Dejarlo", 1)
root.left.right.right.left.left = TreeNode("Tomas aquel papel, era un mapa de una tierra llamada Luprrp. Sigues el mapa y das con una pequeña aldea cuya entrada es tiene forma de un sapo.\nUnos aldeanos te interceptan", "Pedir ayuda", "Esperar", 2)
# root.left.right.right.left.right
root.left.right.right.left.left.left = TreeNode("- Pueden ayudarme ? No sé qué hago aquí\n…Tú escogiste este destino, si no te gusta, vete.", "Seguir hacia la aldea", "Dar la vuelta", 0)
# root.left.right.right.left.left.right
root.left.right.right.left.left.left.left =  ("Caminas solo hacia la aldea, todo el mundo está ocupado en sus labores.\n Parecieran ignorarte...", "Seguir adelante", "Esperar", 3)


current_node = root
count = 0


#####################################################################################################


#####################################################################################################

def Habla(text, action, delay=0.05):
    clear()
    if action != 0:
        draw(action)
    else:
        print(f"[{count}]\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("___________________________________________________________________________________\n")
    for char in text:
        print(char, end='', flush=True)  # Imprime el carácter sin salto de línea
        time.sleep(delay)  # Pausa entre cada carácter
    print()  # Imprime un salto de línea al final

#####################################################################################################


#####################################################################################################

def draw(personaje):

    # Imprimir gato
    if personaje == 1:
        gato = "assets/personajes/gato.txt"
	
        if os.path.isfile(gato):
            with open(gato, "r", encoding="utf-8") as file:
                lines = file.readlines()
                file.seek(0)
        for line in lines:
                print(line.rstrip())

    # Imprimir aldea
    if personaje == 2:
        aldeanos = "assets/personajes/aldeanos.txt"
	
        if os.path.isfile(aldeanos):
            with open(aldeanos, "r", encoding="utf-8") as file:
                lines = file.readlines()
                file.seek(0)
        for line in lines:
                print(line.rstrip())
    
    if personaje == 3:
        aldea = "assets/escenarios/aldea.txt"
	
        if os.path.isfile(aldea):
            with open(aldea, "r", encoding="utf-8") as file:
                lines = file.readlines()
                file.seek(0)
        for line in lines:
                print(line.rstrip())

    if personaje == 4:
        cementerio = "assets/escenarios/cementerio.txt"
	
        if os.path.isfile(cementerio):
            with open(cementerio, "r", encoding="utf-8") as file:
                lines = file.readlines()
                file.seek(0)
        for line in lines:
                print(line.rstrip())


#####################################################################################################


#####################################################################################################

# Función para buscar el nodo correspondiente a la opción seleccionada
def select_option(option):
    global current_node
    # Cuando el nodo esté apuntando a nada
    if current_node is None:
        return None
    
    if option == '1':
        current_node = current_node.left
        return current_node
    elif option == '2':
        current_node = current_node.right
        return current_node
    
    return None

#####################################################################################################


#####################################################################################################

def select_decision(op1, op2):
    global count
    print(f"\n\n\n[1] {op1} \n\n\n[2] {op2}\n")
    print("___________________________________________________________________________________\n")
    r = str(input())
    while r != '1' and r != '2':
        print("\nNo puedo hacer eso...")
        r = str(input())

    count += 1
    read_decision(r)

#####################################################################################################


#####################################################################################################

def read_decision(choice):
    global current_node
    global count
    if count == 1:
        Habla(current_node.text, current_node.action)  # Pasar ambos argumentos 'text' y 'action'
        select_decision(current_node.option1, current_node.option2)


    if count == 2:
        music_thread = threading.Thread(target=select_song, args=(2,))
        music_thread.start()
        
    else:
        current_node = select_option(choice)

    if current_node:
        Habla(current_node.text, current_node.action)  # Pasar ambos argumentos 'text' y 'action'
        select_decision(current_node.option1, current_node.option2)
        select_option()

    else:
        fin = "Fin del juego."
        Habla(fin, 0)  # Pasar 'fin' y un valor de 'action' apropiado
        stop_music()

        
        exit(1)

#####################################################################################################


