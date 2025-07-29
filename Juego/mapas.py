import os
from modulos.menu import cargar_menu
#Variables que determinan cuanto se imprimira de espacio vacio y espacio lleno para crear el mapa
WIDTH_MAPA = 25
HEIHT_MAPA= 15

espacio_vacio = "   "
espacio_lleno= "[ ]"

#por cada cosa en la fila crea un rango de ancho
    #por cada cosa en la fila crea un rango de largo

coordenada_personaje = [5,15]
personaje = "🡱"

def cargar_mapa1(movimiento_personaje):

    # Menu
    cargar_menu()

    os.system("cls")
    if movimiento_personaje == "w":
        personaje = "🡱"
        coordenada_personaje[0] -= 1
    elif movimiento_personaje == "s":
        personaje = "🡳"
        coordenada_personaje[0] += 1
    elif movimiento_personaje == "a":
        personaje = "🡸"
        coordenada_personaje[1] -= 1
    elif movimiento_personaje == "d":
        personaje = "🡺"
        coordenada_personaje[1] += 1
        

        

    print("+"  + "-"*75 + "+")
    for cada_fila in range(HEIHT_MAPA):
        print("|", end="")
        for cada_casilla in range(WIDTH_MAPA):
            if(coordenada_personaje[0] == cada_fila and coordenada_personaje[1]== cada_casilla):
                print(f" {personaje} " ,end= "")
            else:
                print(espacio_vacio, end="")

        print("|") 
    print("+"  + "-"*75 + "+")