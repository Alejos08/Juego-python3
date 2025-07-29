import os
import readchar
from mapas import cargar_mapa1

estado_juego = True
 

def game_1():

    #iniciar juego
    tecla = readchar.readchar()

    if tecla in ("w", "s", "a","d"):
        cargar_mapa1 (tecla)
    elif tecla =="q":
        estado_juego = False



while estado_juego:
    game_1()